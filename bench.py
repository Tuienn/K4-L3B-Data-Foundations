"""Run the shared ecommerce retrieval benchmark for Lab 07.

The script intentionally performs chunking *before* documents reach the
EmbeddingStore.  Change only SELECTED_CHUNKER to compare strategies fairly.
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

from src import (
    EMBEDDING_PROVIDER_ENV,
    GEMINI_EMBEDDING_MODEL,
    LOCAL_EMBEDDING_MODEL,
    OPENAI_EMBEDDING_MODEL,
    Document,
    EmbeddingStore,
    GeminiEmbedder,
    LocalEmbedder,
    OpenAIEmbedder,
    RecursiveChunker,
    _mock_embed,
)

DEFAULT_DATA_DIR = Path("data/ecommerce")
TOP_K = 3

# Change this one line when comparing a different chunking strategy.
SELECTED_CHUNKER = RecursiveChunker(chunk_size=500)


@dataclass(frozen=True)
class BenchmarkCase:
    number: int
    query: str
    gold_answer: str
    source_documents: tuple[str, ...]
    metadata_filter: dict[str, str] | None = None


BENCHMARK_CASES = (
    BenchmarkCase(
        number=1,
        query=(
            "Thời gian tối đa để Người mua gửi yêu cầu Trả hàng/Hoàn tiền "
            "cho Shopee là bao lâu đối với từng loại đơn hàng?"
        ),
        gold_answer=(
            "Thực phẩm tươi sống và đông lạnh: trong vòng 24 giờ kể từ lúc giao hàng "
            "thành công. Đơn Người bán tự vận chuyển: 15 ngày kể từ lúc bấm 'Đã nhận "
            "được hàng', hoặc 20 ngày kể từ lúc 'Lấy hàng thành công' nếu không bấm "
            "nhận hàng. Các đơn hàng thông thường khác: 15 ngày kể từ lúc giao hàng "
            "thành công."
        ),
        source_documents=("quy-dinh-chung-tra-hang-hoan-tien",),
    ),
    BenchmarkCase(
        number=2,
        query=(
            "Những trường hợp hoặc mặt hàng nào không được Shopee chấp nhận trả hàng "
            "do đổi ý hoặc không còn nhu cầu?"
        ),
        gold_answer=(
            "Không hỗ trợ sản phẩm thuộc danh mục hạn chế trả hàng như đồ lót, thực phẩm "
            "tươi sống hoặc thẻ cào; sản phẩm mua tại Shopee Mart; và sản phẩm đã qua sử "
            "dụng hoặc có bao bì, tem mác, niêm phong của nhà sản xuất không còn nguyên vẹn."
        ),
        source_documents=(
            "tra-hang-doi-y-khong-con-nhu-cau",
            "san-pham-han-che-tra-hang",
        ),
    ),
    BenchmarkCase(
        number=3,
        query=(
            "Nếu chọn hình thức 'Tự sắp xếp' cho đơn hàng không thuộc Shopee Mall, "
            "Người mua được hỗ trợ phí trả hàng bằng Shopee Xu như thế nào?"
        ),
        gold_answer=(
            "Cùng tỉnh/thành phố với Người bán được hoàn 25.000 Shopee Xu; khác "
            "tỉnh/thành phố được hoàn 40.000 Shopee Xu. Shopee hỗ trợ trong 3–5 ngày "
            "làm việc sau khi yêu cầu trả hàng được chấp nhận hoàn tiền."
        ),
        source_documents=("phuong-thuc-gui-hang-va-phi-hoan-tra",),
    ),
    BenchmarkCase(
        number=4,
        query=(
            "Khi Người bán gửi đề xuất Hoàn Tiền Ngay, Người mua có những lựa chọn xử lý "
            "nào nếu đồng ý hoặc không đồng ý?"
        ),
        gold_answer=(
            "Nếu đồng ý, chọn 'Trao đổi thêm' rồi nhấn 'Đồng ý' để nhận tiền hoàn ngay "
            "mà không cần gửi trả hàng. Nếu không đồng ý, có thể chọn 'Trao đổi thêm' để "
            "chat thương lượng với Người bán, hoặc chọn 'Tôi muốn trả hàng' để tiếp tục "
            "quy trình trả sản phẩm và nhận toàn bộ số tiền theo yêu cầu ban đầu."
        ),
        source_documents=("nguoi-ban-de-xuat-hoan-tien-ngay",),
        metadata_filter={"audience": "both"},
    ),
    BenchmarkCase(
        number=5,
        query=(
            "Thời gian nhận tiền hoàn vào Ví ShopeePay, SPayLater và Thẻ tín dụng/ghi nợ "
            "mất bao lâu sau khi Shopee chấp nhận hoàn tiền?"
        ),
        gold_answer=(
            "Ví ShopeePay và SPayLater nhận tiền trong vòng 24 giờ khi ví hoạt động bình "
            "thường; tiền hoàn SPayLater vào số dư khả dụng. Thẻ tín dụng/ghi nợ mất 7–14 "
            "ngày làm việc, tùy ngân hàng phát hành thẻ."
        ),
        source_documents=("thoi-gian-va-cach-kiem-tra-tien-hoan",),
    ),
)


def parse_markdown(path: Path) -> tuple[dict[str, str], str]:
    """Return simple YAML front matter and the cleaned Markdown body.

    The lab's data schema is flat key/value YAML, so a dependency on PyYAML is
    unnecessary.  The body is deliberately kept separate from metadata before
    chunking.
    """
    text = path.read_text(encoding="utf-8").replace("\r\n", "\n")
    if not text.startswith("---\n"):
        return {}, text.strip()

    front_matter, delimiter, body = text.partition("\n---\n")
    if not delimiter:
        raise ValueError(f"{path} has an unclosed YAML front matter block")

    front_matter = front_matter.removeprefix("---\n")
    metadata: dict[str, str] = {}
    for line in front_matter.splitlines():
        key, separator, value = line.partition(":")
        if separator:
            metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata, body.strip()


def load_chunked_documents(data_dir: Path) -> list[Document]:
    """Read source files and convert every content chunk into a Document."""
    documents: list[Document] = []
    for path in sorted(data_dir.glob("*.md")):
        metadata, content = parse_markdown(path)
        if not content:
            print(f"Skipping empty content: {path}")
            continue

        doc_id = metadata.get("doc_id", path.stem)
        for index, chunk in enumerate(SELECTED_CHUNKER.chunk(content)):
            documents.append(
                Document(
                    id=f"{doc_id}#{index}",
                    content=chunk,
                    metadata={
                        **metadata,
                        "doc_id": doc_id,
                        "source_file": path.name,
                        "chunk_index": index,
                    },
                )
            )
    return documents


def make_embedder():
    """Match main.py's optional-backend behavior and fall back to mock safely."""
    load_dotenv(override=False)
    provider = os.getenv(EMBEDDING_PROVIDER_ENV, "mock").strip().lower()
    try:
        if provider == "local":
            return LocalEmbedder(os.getenv("LOCAL_EMBEDDING_MODEL", LOCAL_EMBEDDING_MODEL))
        if provider == "openai":
            return OpenAIEmbedder(os.getenv("OPENAI_EMBEDDING_MODEL", OPENAI_EMBEDDING_MODEL))
        if provider == "gemini":
            return GeminiEmbedder(os.getenv("GEMINI_EMBEDDING_MODEL", GEMINI_EMBEDDING_MODEL))
    except Exception as error:
        print(f"Embedding provider '{provider}' is unavailable ({error}); using mock embeddings.")
    return _mock_embed


def print_case_result(case: BenchmarkCase, results: list[dict]) -> None:
    print(f"\n{'=' * 88}\nQuery {case.number}: {case.query}")
    print(f"Gold answer: {case.gold_answer}")
    print(f"Expected source document(s): {', '.join(case.source_documents)}")
    print(f"Metadata filter: {case.metadata_filter or 'none'}")

    if not results:
        print("No chunks matched this query/filter.")
        return

    for rank, result in enumerate(results, start=1):
        metadata = result.get("metadata", {})
        preview = result.get("content", "").replace("\n", " ")[:280]
        print(
            f"\nTop {rank} | score={result.get('score', 0.0):.4f} | "
            f"doc_id={metadata.get('doc_id', 'unknown')} | "
            f"audience={metadata.get('audience', 'unknown')}"
        )
        print(f"{preview}{'...' if len(result.get('content', '')) > 280 else ''}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Run Lab 07 ecommerce retrieval benchmarks.")
    parser.add_argument("--data-dir", type=Path, default=DEFAULT_DATA_DIR)
    parser.add_argument("--top-k", type=int, default=TOP_K)
    args = parser.parse_args()

    if not args.data_dir.is_dir():
        print(f"Data directory not found: {args.data_dir}")
        return 1

    documents = load_chunked_documents(args.data_dir)
    if not documents:
        print("No non-empty Markdown documents were loaded.")
        return 1

    embedder = make_embedder()
    print("=== Ecommerce Retrieval Benchmark ===")
    print(f"Data directory: {args.data_dir}")
    print(f"Chunker: {SELECTED_CHUNKER.__class__.__name__} (chunk_size={SELECTED_CHUNKER.chunk_size})")
    print(f"Embedding backend: {getattr(embedder, '_backend_name', type(embedder).__name__)}")
    print(f"Loaded chunks: {len(documents)}")

    store = EmbeddingStore(collection_name="ecommerce_benchmark", embedding_fn=embedder)
    try:
        store.add_documents(documents)
    except NotImplementedError as error:
        print(f"\nBenchmark cannot run until EmbeddingStore is implemented: {error}")
        return 1

    print(f"Stored chunks: {store.get_collection_size()}")
    for case in BENCHMARK_CASES:
        results = store.search_with_filter(
            case.query,
            top_k=args.top_k,
            metadata_filter=case.metadata_filter,
        )
        print_case_result(case, results)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
