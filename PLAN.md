# Tool tạo Design Checklist từ comment Backlog — Kế hoạch & Phân tích khả thi

> Tài liệu spec + phân tích khả thi cho tool tự động hóa việc biến comment khách hàng Nhật trên Backlog thành design checklist Excel (format 09-CL/PM/VTI).

---

## 1. Bối cảnh & mục tiêu

- **Người dùng:** BrSE/PO trong dự án thiết kế UI/UX POS máy tính bảng (khách Nhật).
- **Pain point:** đọc comment tiếng Nhật trên Backlog rồi gõ tay thành checklist cho designer — chậm, dễ sót.
- **Mục tiêu:** tự động hoá end-to-end, chạy lại được hằng ngày mà không lấy trùng comment cũ.

Tool gồm 2 phần:
1. **MCP server** kết nối Backlog (lọc comment đa điều kiện).
2. **Workflow** comment → checklist Excel đúng format mẫu.

**Ngôn ngữ đề xuất:** Python (xem mục [Lựa chọn ngôn ngữ](#lựa-chọn-ngôn-ngữ-python)).
**Ngôn ngữ comment:** tiếng Nhật (giữ nguyên); UI/log/備考 tiếng Việt.

---

## 2. Tổng quan khả thi

**Kết luận: Khả thi cao.** Cả 2 phần dùng API/library trưởng thành, không rào cản kỹ thuật lớn.
Rủi ro chính: **chất lượng tách rule bằng AI** (Phần 2a), không phải code.

---

## 3. Phần 1 — MCP Server

### 3.1 Tool chính: `get_filtered_comments`

Backlog có 2 API tách biệt → cần **2 tầng filter**:

#### Tầng 1 — Lọc ticket (`GET /api/v2/issues`)
Tham số (optional, hỗ trợ multi-value):
- `projectId[]`, `assigneeId[]`, `createdUserId[]`
- `issueTypeId[]`, `statusId[]`, `categoryId[]`, `milestoneId[]`
- `updatedSince`, `updatedUntil` (YYYY-MM-DD)
- `keyword`
- `count` (max 100, tự phân trang)

#### Tầng 2 — Lấy comment (`GET /api/v2/issues/:issueIdOrKey/comments`)
API chỉ hỗ trợ `minId`, `maxId`, `count` (max 100), `order` → **lọc tiếp trong code**:
- `comment_created_since` / `comment_created_until` (theo field `created`)
- `comment_author_ids[]` (theo `createdUser.id` — vd chỉ lấy comment khách)
- `content_keywords[]` (chỉ giữ comment chứa ít nhất 1 keyword)
- `exclude_change_log_only` (bỏ comment chỉ là log đổi trạng thái, content rỗng/null)

### 3.2 Chống lấy trùng
- File state: `.state/last_comment_ids.json` map `issueId -> maxCommentId` đã xử lý.
- Lần sau gọi `minId = last_max + 1` chỉ lấy comment mới.
- Tham số `force_full=true` để bỏ qua state.
- **Atomic write:** ghi file temp + rename, tránh corrupt nếu interrupt.

### 3.3 Output JSON
```json
[
  {
    "issueKey": "SMJPOS-123",
    "issueSummary": "顧客検索画面",
    "commentId": 456789,
    "created": "2026-05-22T10:30:00Z",
    "authorName": "山田 太郎",
    "authorId": 1001,
    "content": "..."
  }
]
```
Sort: theo `issueKey` rồi `created` ASC.

### 3.4 Yêu cầu kỹ thuật
- Chuẩn MCP đầy đủ (JSON schema cho mọi tham số, mô tả tiếng Việt/Anh).
- Retry + exponential backoff khi gặp **HTTP 429** (Backlog ~150 req/phút/key).
- Đọc secret từ env, **không log API key**.
- README hướng dẫn: cài, đăng ký MCP vào Claude Code, set env.

### 3.5 Tool phụ đề xuất (bổ sung so với prompt gốc)
- **`list_project_users`** — trả `[ {id, name, roleType} ]` để dễ tra `userId` khách hàng, không phải mò thủ công.
- **`list_project_statuses` / `list_project_categories`** — hỗ trợ điền filter chính xác.

### 3.6 Điểm cần lưu ý (gap trong prompt gốc)
| # | Vấn đề | Đề xuất |
|---|---|---|
| 1 | Comment có thể bị **edit** sau khi đã processed | Track thêm `updated` hoặc thêm flag `include_edited` |
| 2 | Backlog có 3 TLD (`.com`, `.jp`, `.backlogtool.com`) | Base URL build từ env, không hardcode |
| 3 | Không có cách tra `userId` khách | Thêm tool `list_project_users` |

---

## 4. Phần 2 — Workflow comment → Checklist

### 4.1 Bước 2a — Tách rule bằng AI **(bottleneck chất lượng)**

Mỗi comment khách thường chia theo màn hình (`【全体】`, `【顧客で検索】`) và nhiều bullet (`・`).
**Mỗi bullet = 1 rule độc lập (atomic).**

#### Cột output cho mỗi rule
| Cột | Nội dung | Ghi chú |
|---|---|---|
| `画面` | Tên màn hình từ tiêu đề 【...】 | `"全体"` nếu thuộc phần chung |
| `カテゴリ` | Phân loại (whitelist cố định bên dưới) | Nếu không khớp → flag để review thủ công |
| `項目` | Đối tượng (vd ボタン, ヘッダー, 明細) | |
| `ルール` | Câu kiểm tra được, tiếng Nhật sạch | Giữ thuật ngữ gốc khách |
| `出典コメントID` | commentId nguồn | Để truy vết |
| `Mandatory` | `◎` / `○` | `○` mặc định; `◎` nếu có `必須`, `必ず`, `必要があります` |
| `備考(VN)` | Giải thích ngắn tiếng Việt | Cho designer VN |

#### Whitelist category (khớp 09-CL/PM/VTI)
```
ヘッダー / フッター / ビジュアルスタイル / コンポーネント動作 /
データフォーマット / レイアウト＆サイズ / ボタン動作 / 入力仕様 /
検索条件 / データ表示 / フォーカス / ラベル
```

#### Cạm bẫy AI
- LLM dễ "sáng tạo" category mới → **validation step**: reject + chọn lại nếu không trong whitelist.
- 1 bullet phức tạp "A và B, ngoài ra C" → cần prompt rõ "tách thành rule atomic".
- Dịch VN chất lượng dao động → giữ thuật ngữ Nhật trong `ルール`, chỉ dịch trong `備考(VN)`.

**Đề xuất:** thêm mode `--dry-run` xuất JSON trung gian để review trước khi ghi Excel.

### 4.2 Bước 2b — Xuất Excel (`.xlsx`)

3 sheet:
| Sheet | Nội dung |
|---|---|
| `表紙` | Tiêu đề + フォーマットコード `09-CL/PM/VTI` + version + 発行日 |
| `変更履歴` | 1 dòng / lần chạy: `No, 日付, 版数, 担当者, 変更内容="comment取込 自動生成"` |
| `チェックリスト` | Bảng rule (cột ở 4.1) + 3 cột rỗng `Round 1 / Round 2 / Round 3` để designer điền ◯/✕/− |

**Format:**
- Font: Meiryo hoặc MS Gothic (hỗ trợ JP).
- Header bold, freeze dòng header, auto-width, có border.
- Tên file: `checklist_<projectKey>_YYYYMMDD.xlsx`.

**Library:** `openpyxl` (Python). KHÔNG dùng `pandas.to_excel` (mất style + xoá data sheet khác khi append).

### 4.3 Bước 2c — Append mode (mặc định BẬT)

| Vấn đề | Cách xử lý |
|---|---|
| Giữ Round 1/2/3 designer đã điền | `load_workbook` rồi append từng row mới — KHÔNG ghi đè |
| Khách edit comment cũ đã có trong file | Policy: bỏ qua / thêm dòng mới `[REVISED]` (cần user quyết) |
| File đang mở trong Excel khi script chạy | Catch `PermissionError`, báo rõ "đóng file Excel rồi chạy lại" |
| Multi-user cùng edit | Khuyến nghị workflow (đóng trước khi chạy, dùng Git/SharePoint version) |

---

## 5. Cấu trúc dự án

```
backlog-checklist/
├── .env.example
├── README.md
├── mcp_server/         # Phần 1: MCP server + Backlog client
│   ├── server.py       # MCP entrypoint
│   ├── backlog_api.py  # HTTP client + rate limit
│   ├── filters.py      # Logic lọc tầng 2
│   └── state.py        # Atomic JSON state
├── pipeline/           # Phần 2: tách rule + xuất Excel
│   ├── extractor.py    # Comment → rules (call LLM)
│   ├── exporter.py     # Rules → xlsx (openpyxl)
│   └── prompts/        # Few-shot prompt templates
├── templates/          # File mẫu 09-CL/PM/VTI (nếu có)
├── tests/              # Test với dữ liệu mock (không gọi Backlog thật)
└── .state/             # State chống trùng (gitignore)
```

---

## 6. Lựa chọn ngôn ngữ: **Python**

| Tiêu chí | Python | Node |
|---|---|---|
| Excel preserve formatting khi append | ✅ `openpyxl` mature | ⚠️ `exceljs` yếu hơn |
| MCP SDK | ✅ `mcp` chính thức | ✅ `@modelcontextprotocol/sdk` |
| Xử lý text Nhật | ✅ `unicodedata`, nhiều ví dụ | ✅ OK |
| Cộng đồng tham khảo | ✅ Nhiều | ⚪ Đủ dùng |

→ **Python.**

---

## 7. Các câu cần xác nhận trước khi code

1. **Domain Backlog cụ thể?** (`.com` / `.jp` / `.backlogtool.com`)
2. **Project key thật?** (vd `SMJPOS`)
3. **userId của khách hàng** — đã biết hay cần tool phụ tra?
4. **File mẫu 09-CL/PM/VTI** — có gửi được không? (tái tạo theo mô tả OK, có mẫu thật thì khớp 100%)
5. **Vị trí lưu file checklist tổng?** (local / OneDrive / SharePoint)
6. **Policy khi comment khách bị edit?** (bỏ qua / thêm dòng `[REVISED]` / cập nhật in-place)

---

## 8. Roadmap đề xuất

| Phase | Nội dung | Trạng thái |
|---|---|---|
| **0** | Xác nhận 6 câu ở mục 7 | ⏳ |
| **1** | Dựng MCP server + tool `get_filtered_comments` + `list_project_users` | ⏳ |
| **1.5** | Dummy pipeline in JSON ra console để verify lấy comment đúng | ⏳ |
| **2a** | Extractor: comment → rules (JSON, dry-run) | ⏳ |
| **2b** | Exporter: rules → Excel sheet đơn | ⏳ |
| **2c** | Append mode + chống trùng | ⏳ |
| **3** | Test end-to-end với comment mẫu (mục 9) | ⏳ |
| **4** | README + đăng ký MCP vào Claude Code | ⏳ |

---

## 9. Comment mẫu để test bước 2a

```
【全体】
・検索条件を未指定の場合は、「進む」ボタンは非活性でお願いします。
・スクロールバーが明細に被らないように調整をお願いします。
【顧客で検索】
・顧客番号→顧客コードに修正をお願いします。
・配送予定日は単一選択です（From～Toではない）ので、修正をお願いします。
```

**Kết quả mong đợi:** 4 dòng rule

| 画面 | カテゴリ | 項目 | ルール | Mandatory | 備考(VN) |
|---|---|---|---|---|---|
| 全体 | ボタン動作 | 「進む」ボタン | 検索条件未指定時は非活性とする | ○ | Khi chưa nhập điều kiện tìm kiếm, nút "Tiếp tục" phải bị disabled |
| 全体 | レイアウト＆サイズ | スクロールバー | 明細に被らないよう配置する | ○ | Thanh cuộn không được đè lên phần chi tiết |
| 顧客で検索 | ラベル | 顧客番号 | ラベルを「顧客コード」に変更する | ○ | Đổi nhãn "顧客番号" thành "顧客コード" |
| 顧客で検索 | 入力仕様 | 配送予定日 | 単一選択とする (From-To ではない) | ○ | Ngày giao hàng dự kiến là chọn 1 ngày, không phải chọn khoảng |

---

## 10. Rủi ro & biện pháp

| Rủi ro | Mức | Biện pháp |
|---|---|---|
| LLM gán sai category | 🔴 Cao | Whitelist validation + few-shot prompt + dry-run review |
| Comment edit không bắt được | 🟡 TB | Track `updated`, thêm flag `include_edited` |
| File Excel đang mở khi chạy | 🟡 TB | Catch + báo lỗi rõ |
| Rate limit 429 | 🟢 Thấp | Retry exponential backoff |
| Mất state file | 🟢 Thấp | Atomic write + backup `.state/last_comment_ids.json.bak` |
| Designer mất công Round columns khi append | 🔴 Cao nếu code sai | Dùng `load_workbook`, KHÔNG dùng pandas |
