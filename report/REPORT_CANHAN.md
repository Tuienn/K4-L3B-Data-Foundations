# Báo Cáo Cá Nhân — Lab 7: Embedding & Vector Store

**Họ tên:** [Tên sinh viên]
**Nhóm:** [Tên nhóm]
**Ngày:** [Ngày nộp]

> **Nộp 1 bản / sinh viên.** Phần nhóm (lựa chọn tài liệu, thiết kế chiến lược, bộ câu hỏi đánh giá, demo) nộp chung 1 bản trong `REPORT_NHOM.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần cá nhân: 60** = Khởi động (5) + Hướng tiếp cận (10) + Hoàn thiện code (30) + Dự đoán độ tương tự (5) + Kết quả truy xuất của tôi (10).

---

## 1. Khởi động (Warm-up) — Cá nhân (5 điểm)

### Độ tương tự Cosine (Cosine Similarity) (Bài tập 1.1)

**Độ tương tự cosine cao (High cosine similarity) nghĩa là gì?**
> Hai văn bản có hướng biểu diễn embedding gần nhau, tức chúng có ý nghĩa hoặc ngữ cảnh tương tự. Điểm càng gần 1 thì mức độ tương đồng ngữ nghĩa càng cao.

**Ví dụ có độ tương tự CAO:**
- Câu A: Tôi muốn đổi trả chiếc áo đã mua.
- Câu B: Làm thế nào để hoàn tiền cho sản phẩm không phù hợp?
- Tại sao tương đồng: Hai câu diễn đạt bằng từ khác nhau nhưng cùng nói về nhu cầu đổi trả/hoàn tiền sau khi mua hàng.

**Ví dụ có độ tương tự THẤP:**
- Câu A: Chính sách bảo hành điện thoại kéo dài bao lâu?
- Câu B: Hôm nay trời có mưa không?
- Tại sao khác: Hai câu thuộc hai chủ đề và mục đích hoàn toàn khác nhau: một câu hỏi về chính sách sản phẩm, câu còn lại hỏi thời tiết.

**Tại sao độ tương tự cosine (cosine similarity) được ưu tiên hơn khoảng cách Euclid (Euclidean distance) cho text embeddings?**
> Cosine similarity so sánh góc giữa các vector, nên tập trung vào hướng ngữ nghĩa thay vì độ lớn của vector. Với text embedding, hai câu cùng nghĩa vẫn nên gần nhau dù vector của chúng có độ dài khác nhau; vì vậy cosine thường phù hợp hơn khoảng cách Euclid.

### Bài toán tính toán Chunking (Bài tập 1.2)

**Tài liệu 10,000 ký tự, chunk_size=500, overlap=50. Bao nhiêu chunks?**
> *Trình bày phép tính:* `ceil((10000 - 50) / (500 - 50)) = ceil(9950 / 450) = ceil(22,11)`
> *Đáp án:* **23 chunks**.

**Nếu độ chồng chéo (overlap) tăng lên 100, số lượng chunk thay đổi thế nào? Tại sao muốn độ chồng chéo nhiều hơn?**
> Với `overlap=100`: `ceil((10000 - 100) / (500 - 100)) = ceil(9900 / 400) = ceil(24,75) = 25`, nên số chunk tăng từ 23 lên **25**. Overlap lớn hơn giữ lại ngữ cảnh ở ranh giới giữa hai chunk, giảm nguy cơ một ý hoặc câu trả lời bị cắt rời; đánh đổi là cần lưu trữ và xử lý nhiều chunk hơn.

---

## 2. Hướng tiếp cận của tôi (My Approach) — Cá nhân (10 điểm)

Giải thích cách tiếp cận của bạn khi lập trình (implement) các phần chính trong gói `src`.

### Các hàm chia nhỏ (Chunking Functions)

**`SentenceChunker.chunk`** — hướng tiếp cận:
> *Viết 2-3 câu: dùng biểu thức chính quy (regex) gì để phát hiện câu? Xử lý trường hợp ngoại lệ (edge case) nào?*

**`RecursiveChunker.chunk` / `_split`** — hướng tiếp cận:
> *Viết 2-3 câu: thuật toán hoạt động thế nào? Base case (trường hợp cơ sở) là gì?*

### Lớp EmbeddingStore

**`add_documents` + `search`** — hướng tiếp cận:
> *Viết 2-3 câu: lưu trữ thế nào? Tính độ tương tự ra sao?*

**`search_with_filter` + `delete_document`** — hướng tiếp cận:
> *Viết 2-3 câu: lọc (filter) trước hay sau? Xóa bằng cách nào?*

### Tác tử KnowledgeBaseAgent

**`answer`** — hướng tiếp cận:
> *Viết 2-3 câu: cấu trúc prompt? Cách đưa ngữ cảnh (inject context) vào thế nào?*

---

## 3. Hoàn thiện code (Core Implementation) — Cá nhân (30 điểm)

Vượt qua bộ kiểm thử là điều kiện tính điểm phần này.

### Kết Quả Kiểm Thử (Test Results)

```
# Dán kết quả (output) của: pytest tests/ -v
```

**Số lượng bài test vượt qua (pass):** __ / 42

---

## 4. Dự đoán độ tương tự (Similarity Predictions) — Cá nhân (5 điểm)

| Cặp | Câu A | Câu B | Dự đoán | Điểm thực tế | Đúng? |
|------|-----------|-----------|---------|--------------|-------|
| 1 | | | cao / thấp | | |
| 2 | | | cao / thấp | | |
| 3 | | | cao / thấp | | |
| 4 | | | cao / thấp | | |
| 5 | | | cao / thấp | | |

**Kết quả nào bất ngờ nhất? Điều này nói gì về cách embeddings biểu diễn ý nghĩa?**
> *Viết 2-3 câu:*

---

## 5. Kết quả truy xuất của tôi (Competition Results) — Cá nhân (10 điểm)

Chạy **5 câu hỏi đánh giá của nhóm** trên mã nguồn cá nhân của bạn trong gói `src`. **5 câu hỏi này phải trùng với các thành viên cùng nhóm** (xem `REPORT_NHOM.md`).

| # | Câu hỏi (Query) | Top-1 Chunk truy xuất được (tóm tắt) | Điểm Score | Có liên quan không? (Relevant) | Câu trả lời của Agent (tóm tắt) |
|---|-------|--------------------------------|-------|-----------|------------------------|
| 1 | Thời gian tối đa gửi yêu cầu Trả hàng/Hoàn tiền theo từng loại đơn hàng là bao lâu? | Chunk từ `quy-dinh-chung-tra-hang-hoan-tien` nêu trực tiếp mốc 24 giờ cho thực phẩm tươi sống/đông lạnh, 15/20 ngày cho đơn tự vận chuyển và 15 ngày cho đơn khác. | 0.8758 | Có — top-1 chứa đủ thông tin của gold answer. | Chưa chạy trong `bench.py`; ngữ cảnh top-1 đủ để agent trả lời có căn cứ. |
| 2 | Trường hợp hoặc mặt hàng nào không được trả hàng do đổi ý/không còn nhu cầu? | Top-1 từ `san-pham-han-che-tra-hang` xác định nhóm hàng hạn chế trả hàng; top-2 từ `tra-hang-doi-y-khong-con-nhu-cau` nêu hàng đã dùng, mất seal hoặc hàng điện tử đã kích hoạt. | 0.9081 | Có trong top-3, nhưng phải kết hợp nhiều chunk; dữ liệu nguồn không nêu Shopee Mart. | Chưa chạy; không nên khẳng định ý “Shopee Mart” vì chưa có evidence trong corpus. |
| 3 | Với hình thức Tự sắp xếp, đơn không thuộc Shopee Mall được hoàn Shopee Xu thế nào? | Chunk từ `phuong-thuc-gui-hang-va-phi-hoan-tra` nêu hoàn 25.000 Xu cùng tỉnh và 40.000 Xu khác tỉnh sau khi yêu cầu được chấp nhận. | 0.7956 | Có — top-1 chứa thông tin chính; cùng section cũng nêu mốc hỗ trợ 3–5 ngày làm việc. | Chưa chạy trong `bench.py`; ngữ cảnh top-1 đủ để agent tổng hợp gold answer. |
| 4 | Nếu Người bán đề xuất Hoàn Tiền Ngay, Người mua xử lý thế nào khi đồng ý/không đồng ý? (`audience=both`) | Top-1 là bối cảnh quy trình; top-2 nêu cách đồng ý và top-3 nêu hai cách không đồng ý. Cả ba đều từ `nguoi-ban-de-xuat-hoan-tien-ngay`. | 0.8716 | Có trong top-3, nhưng top-1 riêng lẻ chưa đủ chi tiết. Filter `audience=both` chọn đúng phạm vi. | Chưa chạy; agent cần tổng hợp top-2 và top-3 để trả lời đầy đủ. |
| 5 | Tiền hoàn về ShopeePay, SPayLater và thẻ tín dụng/ghi nợ mất bao lâu? | Top-1 chỉ là header bảng; top-2 là phần giới thiệu; top-3 xác nhận ví ShopeePay hoạt động bình thường được hoàn trong 24 giờ. | 0.8693 | Có liên quan, nhưng top-3 chưa chứa đủ mốc SPayLater và thẻ tín dụng/ghi nợ. | Chưa chạy; top-3 hiện chưa đủ grounding để trả lời trọn gold answer. |

**Bao nhiêu câu hỏi trả về chunk có liên quan trong top-3?** **5 / 5** *(đánh giá độ liên quan theo retrieval; 3/5 có đủ evidence top-3 để trả lời trọn gold answer: câu 1, 3 và 4).*

**Phân tích kết quả benchmark:**
> Benchmark dùng `RecursiveChunker(chunk_size=500)`, 182 chunks và `gemini-embedding-001`. Retrieval theo nguồn đạt tốt: cả 5 query đều có chunk liên quan trong top-3 và truy xuất đúng tài liệu nguồn chính ở top-1 hoặc top-2. Điểm score nằm trong khoảng 0.7956–0.9081, cho thấy embedding Gemini phân biệt ngữ nghĩa tốt hơn mock embedder.
>
> Hai failure case quan trọng là câu 5 và câu 2. Ở câu 5, bảng Markdown có nhiều URL dài bị RecursiveChunker cắt thành các mảnh, nên top-3 chỉ có header/giới thiệu/điều kiện ShopeePay thay vì đủ ba phương thức thanh toán. Ở câu 2, gold answer có ý “sản phẩm mua tại Shopee Mart”, nhưng nội dung này không xuất hiện trong hai tài liệu nguồn đã chỉ định; đây là lỗi thiết kế benchmark chứ không thể coi là lỗi retrieval.
>
> Nếu làm lại, tôi sẽ làm sạch URL và ảnh trước khi chunk, giữ nguyên từng bảng Markdown như một block hoặc dùng chunker theo heading/bảng với fallback recursive. Tôi cũng sẽ sửa gold answer câu 2 để chỉ chứa thông tin có trong corpus, hoặc bổ sung một tài liệu công khai có chính sách Shopee Mart.

**Điều hay nhất tôi học được từ thành viên khác / nhóm khác (qua demo):**
> Kết quả cho thấy kiểm tra đúng `doc_id` là chưa đủ: một chunk đúng tài liệu vẫn có thể chỉ là tiêu đề hoặc bối cảnh và không đủ để trả lời. Việc xem trực tiếp top-3 giúp phát hiện lỗi cắt bảng, đồng thời cho thấy metadata filter chỉ thực sự có ích khi corpus có các nhóm `audience` cạnh tranh nhau.

---

## Tự Đánh Giá (Phần Cá Nhân)

| Tiêu chí | Điểm tự đánh giá |
|----------|-------------------|
| Khởi động (Warm-up) | / 5 |
| Hướng tiếp cận của tôi (My Approach) | / 10 |
| Hoàn thiện code (Core Implementation — tests) | / 30 |
| Dự đoán độ tương tự (Similarity Predictions) | / 5 |
| Kết quả truy xuất của tôi (Competition Results) | / 10 |
| **Tổng phần cá nhân** | **/ 60** |
