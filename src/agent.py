from typing import Callable

from .store import EmbeddingStore


class KnowledgeBaseAgent:
    """
    An agent that answers questions using a vector knowledge base.

    Retrieval-augmented generation (RAG) pattern:
        1. Retrieve top-k relevant chunks from the store.
        2. Build a prompt with the chunks as context.
        3. Call the LLM to generate an answer.
    """

    def __init__(self, store: EmbeddingStore, llm_fn: Callable[[str], str]) -> None:
        self.store = store
        self.llm_fn = llm_fn

    def answer(self, question: str, top_k: int = 3) -> str:
        if self.store.get_collection_size() == 0:
            return "Không tìm thấy tài liệu nào trong cơ sở tri thức để trả lời câu hỏi này."

        results = self.store.search(question, top_k=top_k)
        if not results:
            return "Không tìm thấy ngữ cảnh phù hợp trong cơ sở tri thức để trả lời câu hỏi này."

        context_parts: list[str] = []
        for index, result in enumerate(results, start=1):
            metadata = result.get("metadata", {})
            source = (
                metadata.get("source_file")
                or metadata.get("title")
                or metadata.get("doc_id")
                or result.get("id", "unknown")
            )
            context_parts.append(f"[{index}] Source: {source}\n{result['content']}")

        context = "\n\n".join(context_parts)
        prompt = f"""Bạn là trợ lý tri thức. Chỉ trả lời dựa trên ngữ cảnh được cung cấp.
Nếu ngữ cảnh không đủ để trả lời, hãy nói rõ rằng bạn không tìm thấy thông tin.
Khi trả lời, hãy trích dẫn số nguồn liên quan dưới dạng [1], [2].

Ngữ cảnh:
{context}

Câu hỏi: {question}

Trả lời:"""
        return self.llm_fn(prompt)
