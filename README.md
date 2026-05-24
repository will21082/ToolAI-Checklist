# ToolAI-Checklist

Tool tự động hóa toàn bộ quy trình từ **comment khách hàng Nhật trên Backlog** → **Design Review Checklist** → **Google Sheets** để designer check off từng hạng mục.

Chạy bằng **Claude Code** + MCP server Backlog + Google Sheets API.

---

## Mục đích

Trước đây: BrSE/PO đọc comment Backlog → tổng hợp thủ công → gửi file cho designer → designer không biết ưu tiên cái gì.

Sau khi dùng tool này:

1. Gõ 1 lệnh trong Claude Code → tool tự kéo toàn bộ comment khách từ Backlog
2. AI phân tích, gom nhóm theo ticket + 親課題, viết thành "việc cần sửa" rõ ràng
3. Xuất file Markdown → tự convert CSV → upload Google Sheets với format đẹp, checkbox sẵn
4. Designer nhận link Sheets → đọc là biết ngay cần sửa gì, check ✓ từng dòng

---

## Architecture

```
┌──────────────────────────────────────────────────────────────────────┐
│  PHASE 1 — Tạo Checklist                                             │
│                                                                      │
│   👤 BrSE/PO                                                         │
│       │  yêu cầu tạo checklist (assignee, status, 親課題)            │
│       ▼                                                              │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  Claude Code (IDE)                                          │    │
│  │                                                             │    │
│  │  Skill: backlog-to-checklist  ◄── Checklist_Screen_        │    │
│  │  - phân tích comment               Design_VN.md            │    │
│  │  - gom nhóm theo ticket            (bộ category chuẩn)     │    │
│  │  - viết "việc cần sửa"                                      │    │
│  │                                                             │    │
│  │  Gọi MCP tools:                                             │    │
│  │  ┌─────────────────────────────────────────────────────┐   │    │
│  │  │  MCP Server: backlog                                │   │    │
│  │  │  (cài sẵn, kết nối Backlog Cloud bên trong)         │   │    │
│  │  │                                                     │   │    │
│  │  │  get_issues        → lấy danh sách ticket           │   │    │
│  │  │  get_issue_comments → lấy comment từng ticket       │   │    │
│  │  │  get_issue          → resolve parentIssueId         │   │    │
│  │  └─────────────────────────────────────────────────────┘   │    │
│  └──────────────────────────────┬──────────────────────────────┘    │
│                                 │                                    │
│                                 ▼                                    │
│                    output/Checklist_*.md                             │
└──────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────┐
│  PHASE 2 — Upload Google Sheets                                      │
│                                                                      │
│                    output/Checklist_*.md                             │
│                                 │                                    │
│                                 ▼                                    │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │  scripts/run_all.py  (1 lệnh duy nhất)                      │    │
│  │                                                             │    │
│  │  md_to_csv.py       Markdown → CSV 15 cột                  │    │
│  │       ↓                                                     │    │
│  │  upload_to_gdrive.py  upload + format tự động:             │    │
│  │                       merge cells, checkbox Round 1/2/3,   │    │
│  │                       màu theo category, freeze 3 cột      │    │
│  │                                                             │    │
│  │  Gọi Google APIs (qua OAuth2 Desktop):                      │    │
│  │  ┌─────────────────────────────────────────────────────┐   │    │
│  │  │  Google Drive API v3  → tạo file hoặc thêm tab mới  │   │    │
│  │  │  Google Sheets API v4 → format, merge, checkbox      │   │    │
│  │  └─────────────────────────────────────────────────────┘   │    │
│  └──────────────────────────────┬──────────────────────────────┘    │
│                                 │                                    │
│                                 ▼                                    │
│  📊 Google Sheets (1 file, nhiều tab theo ngày)                     │
│     Tab: Checklist_DaModoshi_VTI_アイン_2026-05-24                  │
│     Tab: Checklist_KakuninMachi_VTI_アイン_2026-05-24               │
│                                 │                                    │
│                                 ▼                                    │
│              👤 Designer check ✓ Round 1 / Round 2 / Round 3        │
└──────────────────────────────────────────────────────────────────────┘
```

---

## Luồng xử lý

### Phase 1 — Tạo Checklist (Claude Code)

| Bước | Mô tả |
|------|-------|
| **1. Thu thập** | `get_issues` với `assigneeId` + `statusId` + `count=100` (tự pagination nếu ≥100) |
| **2. Lọc** | Chỉ giữ comment thiết kế của khách, bỏ log trạng thái rỗng |
| **3. Nhóm** | Gom comment theo từng ticket; resolve `parentIssueId` → nhãn 親課題 |
| **4. Chuyển đổi** | Mỗi ý → 1 dòng mệnh lệnh rõ việc (KHÔNG viết câu hỏi) |
| **5. Xuất** | 1 file `.md` trong `output/`, tách theo 親課題 + từng ticket |

### Phase 2 — Upload Google Sheets (Python scripts)

| Bước | Lệnh / File | Mô tả |
|------|-------------|-------|
| **1. Convert** | `md_to_csv.py` | Parse Markdown → CSV 15 cột |
| **2. Upload** | `upload_to_gdrive.py` | Upload CSV → Google Sheets |
| **3. Format** | (tự động) | Merge cells, checkbox Round 1/2/3, màu theo category, freeze 3 cột |
| **4. Pipeline** | `run_all.py` | Gộp 3 bước trên thành 1 lệnh, tự nhớ spreadsheet ID |

---

## Cấu trúc thư mục

```
ToolAI-Checklist/
├── .claude/
│   └── skills/
│       └── backlog-to-checklist/
│           ├── SKILL.md                       # Định nghĩa skill + quy trình AI
│           └── Checklist_Screen_Design_VN.md  # Bộ category chuẩn (tham chiếu)
├── scripts/
│   ├── run_all.py             # Pipeline 1 lệnh: .md → CSV → Sheets
│   ├── md_to_csv.py           # Convert Markdown checklist → CSV
│   └── upload_to_gdrive.py    # Upload CSV → Google Sheets + format
├── output/
│   └── Checklist_<loại>_<assignee>_YYYY-MM-DD.md   # File checklist (được commit)
├── requirements.txt           # Python dependencies
├── credentials.json           # ← KHÔNG commit (lấy từ Google Cloud Console)
├── token.json                 # ← KHÔNG commit (tự tạo sau lần auth đầu)
├── .state/
│   └── spreadsheet.json       # ← KHÔNG commit (lưu spreadsheet ID tự động)
├── .gitignore
└── README.md
```

---

## Setup máy mới (lần đầu)

### 1. Clone repo

```bash
git clone https://github.com/will21082/ToolAI-Checklist.git
cd ToolAI-Checklist
```

### 2. Cài Python dependencies

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 3. Lấy `credentials.json` từ Google Cloud Console

> File này **không được commit** vì chứa client secret — phải lấy thủ công.

1. Vào [Google Cloud Console](https://console.cloud.google.com) → chọn project cũ
2. **APIs & Services → Credentials**
3. Click vào OAuth 2.0 Client ID loại **Desktop app** → **Download JSON**
4. Đặt file vào thư mục gốc project, đổi tên thành `credentials.json`

> **Lưu ý:** Phải là loại **Desktop app**, không phải Web application.
> Nếu chưa bật API: cần bật **Google Drive API** và **Google Sheets API** trong Cloud Console.

### 4. Chạy lần đầu (mở trình duyệt để xác thực)

```bash
.venv/bin/python3 scripts/run_all.py
```

Trình duyệt tự mở → đăng nhập Google → cấp quyền → đóng lại.
File `token.json` được tạo tự động. Spreadsheet ID đã được lưu sẵn trong `.state/spreadsheet.json` — script tự dùng đúng file Sheets, không cần config thêm gì.

---

## Sử dụng hàng ngày

```bash
# Chạy với file .md mới nhất trong output/ (tự detect)
.venv/bin/python3 scripts/run_all.py

# Chỉ định file cụ thể
.venv/bin/python3 scripts/run_all.py output/Checklist_xxx.md

# Tạo file Google Sheets mới (thay vì thêm tab vào file đang có)
.venv/bin/python3 scripts/run_all.py --new-file
```

Mỗi lần chạy → thêm 1 tab mới vào cùng file Google Sheets (tên tab = tên file `.md`).
Nếu tab đã tồn tại → tự xóa và tạo lại (refresh data).

---

## Columns Google Sheets

| Cột | Mô tả |
|-----|-------|
| 親課題 | Ticket cha (merge theo group) |
| Ticket | Issue key (merge theo ticket) |
| Tiêu đề màn hình | Tên màn hình (merge theo ticket) |
| # | Số thứ tự trong ticket |
| Nhóm | Category (màu riêng theo loại) |
| Việc cần sửa | Mô tả việc cần làm — mệnh lệnh rõ ràng |
| 出典 | Comment ID nguồn để truy vết |
| Round 1 / 2 / 3 | Checkbox ✓ designer tự điền |
| M | Mandatory — chỉ đánh khi khách dùng 必須/必ず |
| Remark | Ghi chú điểm dễ sót |
| Người phụ trách | Assignee (merge theo ticket) |
| Status | Trạng thái ticket (merge theo ticket) |
| Ngày comment | Ngày khách comment (merge theo ticket) |

---

## Quy tắc quan trọng

- **Cột "Việc cần sửa"** luôn là mệnh lệnh rõ việc — KHÔNG viết câu hỏi (`...chưa?`, `...không?`)
- **Lọc assignee** dùng `assigneeId=[id số]` — KHÔNG dùng `keyword`
- **Mandatory (M)** — chỉ đánh khi khách dùng từ mạnh: 必須 / 必ず / 絶対 / "bắt buộc"
- **Không sửa Backlog** — chỉ đọc, không ghi/sửa/xóa comment khách

---

## Thông tin dự án (POS UI)

| | |
|---|---|
| Project | POS_UI (`id: 745282`) |
| VTI アイン `assigneeId` | `2045991` |
| Status 差戻／修正依頼 | `id: 379481` |
| Status 確認待ち | `id: 379472` |
| Google Sheets chính | `.state/spreadsheet.json` (tự tạo sau lần chạy đầu) |
