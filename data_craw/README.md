# Dữ Liệu Shopee Help Center: Trả Hàng & Hoàn Tiền

- **Nguồn chuyên mục:** [https://help.shopee.vn/portal/4/category/61-Tr%25E1%25BA%25A3-H%25C3%25A0ng-Ho%25C3%25A0n-Ti%25E1%25BB%2581n/](https://help.shopee.vn/portal/4/category/61-Tr%25E1%25BA%25A3-H%25C3%25A0ng-Ho%25C3%25A0n-Ti%25E1%25BB%2581n/)
- **Frontend Portal:** Shopee Người mua (Portal 4)
- **Category ID:** 61 (Trả Hàng & Hoàn Tiền)
- **Ngày thu thập (`retrieved_at`):** 2026-09-20
- **Tổng số tài liệu:** 17 bài viết

---

## 1. Cấu Trúc Thư Mục `data_craw/`

```text
data_craw/
├── *.md                    # Toàn bộ 17 bài viết dạng Markdown phẳng (sẵn sàng nạp RAG/Chunking)
├── by_category/            # Phân nhóm bài viết theo từng danh mục con
│   ├── 01_nhung-quy-dinh-chung-ve-tra-hang-hoan-tien/
│   ├── 02_gui-yeu-cau-tra-hang/
│   ├── 03_theo-doi-yeu-cau-tra-hang/
│   ├── 04_shopee-xem-xet/
│   ├── 05_tra-hang/
│   ├── 06_nguoi-ban-khieu-nai/
│   └── 07_hoan-tien/
├── raw_json/               # Toàn bộ dữ liệu phản hồi JSON gốc từ API Shopee
├── metadata.json           # Danh sách và siêu dữ liệu tổng hợp
└── README.md               # Tài liệu này
```

---

## 2. Bảng Thống Kê Tài Liệu (Exercise 3.0 Manifest)

| # | ID | Tên tài liệu | Danh mục con | Nguồn (Source URL) | Số ký tự | Số từ | File |
|---|---|---|---|---|---:|---:|---|
| 1 | 79061 | [Trả hàng/ Hoàn tiền] Các phương thức gửi hàng hoàn trả và phí hoàn trả | Trả hàng | [https://help.shopee.vn/portal/4/article/79061](https://help.shopee.vn/portal/4/article/79061) | 7,120 | 1,248 | `79061-tra-hang-hoan-tien-cac-phuong-thuc-gui-hang-hoan-tra-va-phi-.md` |
| 2 | 79131 | [Trả hàng/ Hoàn tiền] Các phương thức gửi hàng hoàn trả và phí hoàn trả | Trả hàng | [https://help.shopee.vn/portal/4/article/79131](https://help.shopee.vn/portal/4/article/79131) | 7,120 | 1,248 | `79131-tra-hang-hoan-tien-cac-phuong-thuc-gui-hang-hoan-tra-va-phi-.md` |
| 3 | 79137 | [Trả hàng/Hoàn tiền] Những quy định chung về Trả hàng/Hoàn tiền của Shopee | Những quy định chung về Trả hàng/ Hoàn tiền | [https://help.shopee.vn/portal/4/article/79137](https://help.shopee.vn/portal/4/article/79137) | 6,693 | 1,301 | `79137-tra-hanghoan-tien-nhung-quy-dinh-chung-ve-tra-hanghoan-tien-.md` |
| 4 | 79233 | [Trả hàng/ Hoàn tiền] Hướng dẫn gửi yêu cầu Trả hàng/ Hoàn tiền | Gửi yêu cầu trả hàng | [https://help.shopee.vn/portal/4/article/79233](https://help.shopee.vn/portal/4/article/79233) | 2,396 | 490 | `79233-tra-hang-hoan-tien-huong-dan-gui-yeu-cau-tra-hang-hoan-tien.md` |
| 5 | 79258 | [Trả hàng/Hoàn tiền] Cẩm nang Trả hàng hoàn tiền | Gửi yêu cầu trả hàng | [https://help.shopee.vn/portal/4/article/79258](https://help.shopee.vn/portal/4/article/79258) | 4,946 | 411 | `79258-tra-hanghoan-tien-cam-nang-tra-hang-hoan-tien.md` |
| 6 | 79298 | [Trả hàng/ Hoàn tiền] Theo dõi tình trạng Trả hàng/ Hoàn tiền trên Shopee | Theo dõi yêu cầu trả hàng | [https://help.shopee.vn/portal/4/article/79298](https://help.shopee.vn/portal/4/article/79298) | 1,933 | 250 | `79298-tra-hang-hoan-tien-theo-doi-tinh-trang-tra-hang-hoan-tien-tr.md` |
| 7 | 79465 | [Trả hàng/ Hoàn tiền] Sản phẩm hạn chế trả hàng là gì? | Những quy định chung về Trả hàng/ Hoàn tiền | [https://help.shopee.vn/portal/4/article/79465](https://help.shopee.vn/portal/4/article/79465) | 1,192 | 259 | `79465-tra-hang-hoan-tien-san-pham-han-che-tra-hang-la-gi.md` |
| 8 | 79467 | [Trả hàng/Hoàn tiền] Hướng dẫn chuẩn bị bằng chứng khi yêu cầu Trả hàng/ Hoàn tiền | Gửi yêu cầu trả hàng | [https://help.shopee.vn/portal/4/article/79467](https://help.shopee.vn/portal/4/article/79467) | 3,620 | 681 | `79467-tra-hanghoan-tien-huong-dan-chuan-bi-bang-chung-khi-yeu-cau-.md` |
| 9 | 79508 | [Trả hàng/ Hoàn tiền] Cách đóng gói đơn hàng hoàn trả | Trả hàng | [https://help.shopee.vn/portal/4/article/79508](https://help.shopee.vn/portal/4/article/79508) | 4,544 | 721 | `79508-tra-hang-hoan-tien-cach-dong-goi-don-hang-hoan-tra.md` |
| 10 | 164831 | [Trả hàng/Hoàn tiền] Làm sao để kiểm tra tiền đã hoàn vào SPayLater hay chưa? | Hoàn tiền | [https://help.shopee.vn/portal/4/article/164831](https://help.shopee.vn/portal/4/article/164831) | 6,002 | 1,132 | `164831-tra-hanghoan-tien-lam-sao-de-kiem-tra-tien-da-hoan-vao-spayl.md` |
| 11 | 188931 | [Trả hàng/Hoàn tiền] Những quy định chung về Trả hàng/Hoàn tiền của Shopee | Những quy định chung về Trả hàng/ Hoàn tiền | [https://help.shopee.vn/portal/4/article/188931](https://help.shopee.vn/portal/4/article/188931) | 6,693 | 1,301 | `188931-tra-hanghoan-tien-nhung-quy-dinh-chung-ve-tra-hanghoan-tien-.md` |
| 12 | 189473 | [Trả hàng/ Hoàn tiền] Thời gian nhận tiền hoàn và cách kiểm tra tiền hoàn | Hoàn tiền | [https://help.shopee.vn/portal/4/article/189473](https://help.shopee.vn/portal/4/article/189473) | 5,783 | 732 | `189473-tra-hang-hoan-tien-thoi-gian-nhan-tien-hoan-va-cach-kiem-tra.md` |
| 13 | 189476 | [Trả hàng/ Hoàn tiền] Cách theo dõi tình trạng vận chuyển hàng hoàn trả | Trả hàng | [https://help.shopee.vn/portal/4/article/189476](https://help.shopee.vn/portal/4/article/189476) | 2,242 | 148 | `189476-tra-hang-hoan-tien-cach-theo-doi-tinh-trang-van-chuyen-hang-.md` |
| 14 | 189477 | [Trả hàng/ Hoàn tiền] Các phương thức gửi hàng hoàn trả và phí hoàn trả | Trả hàng | [https://help.shopee.vn/portal/4/article/189477](https://help.shopee.vn/portal/4/article/189477) | 7,120 | 1,248 | `189477-tra-hang-hoan-tien-cac-phuong-thuc-gui-hang-hoan-tra-va-phi-.md` |
| 15 | 190242 | [Trả hàng/ Hoàn tiền] Quy trình Shopee xử lý yêu cầu Trả hàng/ Hoàn tiền | Shopee xem xét | [https://help.shopee.vn/portal/4/article/190242](https://help.shopee.vn/portal/4/article/190242) | 8,624 | 1,701 | `190242-tra-hang-hoan-tien-quy-trinh-shopee-xu-ly-yeu-cau-tra-hang-h.md` |
| 16 | 190387 | [Trả hàng/ Hoàn tiền] Hướng dẫn Người mua trả lời đề xuất Hoàn Tiền Ngay của Người bán | Người bán khiếu nại | [https://help.shopee.vn/portal/4/article/190387](https://help.shopee.vn/portal/4/article/190387) | 1,609 | 231 | `190387-tra-hang-hoan-tien-huong-dan-nguoi-mua-tra-loi-de-xuat-hoan-.md` |
| 17 | 204305 | Những điều cần biết về Trả hàng do "Đổi ý/không còn nhu cầu" | Những quy định chung về Trả hàng/ Hoàn tiền | [https://help.shopee.vn/portal/4/article/204305](https://help.shopee.vn/portal/4/article/204305) | 7,404 | 1,582 | `204305-nhung-dieu-can-biet-ve-tra-hang-do-doi-ykhong-con-nhu-cau.md` |

---

## 3. Cấu Trúc Siêu Dữ Liệu (Metadata Schema) Mỗi Tài Liệu

Mỗi file `.md` đều chứa phần YAML frontmatter ở đầu file:

```yaml
---
doc_id: "shopee-returns-<id>"
article_id: <id>
title: "<Tiêu đề bài viết>"
audience: "buyer"
category: "Trả Hàng & Hoàn Tiền"
category_id: 61
sub_category: "<Tên danh mục con>"
sub_category_id: <id danh mục con>
language: "vi"
source_url: "https://help.shopee.vn/portal/4/article/<id>"
retrieved_at: "2026-09-20"
document_version: "1.0"
character_count: <số ký tự>
word_count: <số từ>
---
```
