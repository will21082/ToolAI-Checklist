# SHARP POS UI — Design Review Checklist
> VTI アイン · 20_確認待ち · 2026-05-24 · Chuẩn: Checklist_Screen_Design_VN.md

| | |
|---|---|
| Tổng tickets | 3 |
| Tổng việc cần sửa | 5 |
| Khoảng ngày comment | 2026-05-12 ～ 2026-05-14 |
| Điều kiện lọc | assignee = VTI アイン · status = 20_確認待ち · assigneeId=2045991 |

**Cách dùng:** Sửa xong từng dòng → check ✓ Round 1 → khi tất cả xong → upload → đổi status Backlog `40_対応済み／確認依頼`.

---

# 親課題: [POS_UI-5] 売上返品・売上内容変更

---

## [POS_UI-199] 返金決済画面
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI アイン
- Status: 20_確認待ち
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | UI Components & Controls | Xác nhận lý do グレーアウト của「代引」「株主優待券」với SMJ 河野; bổ sung tooltip hoặc chú thích vào thiết kế nếu cần | c-735374752 | | | | | SMJ hỏi lý do, cần phản hồi và cập nhật design nếu thiếu giải thích |

---

# 親課題: [POS_UI-134] 見積書未承認一覧(配送端末)

---

## [POS_UI-164] C000119_フリー入力
- 親課題: [POS_UI-134] 見積書未承認一覧(配送端末)
- Người phụ trách: VTI アイン
- Status: 20_確認待ち
- Ngày comment: 2026-05-12 ～ 2026-05-14 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Tab & Thông tin Chi tiết / Consistency | Thêm tab「次回訪問予定」～「コメント」vào màn C000114_詳細 | c-736196286 | | | | | Tham chiếu POS_UI-160#comment-736195478 |
| 2 | Screen Flow & Luồng Xử lý | Xác nhận luồng フリー入力: khi chọn「フリー入力」trong C000118_見積結果 → nhập tay thay vì chọn từ danh sách; bổ sung màn nhập tay nếu chưa có | c-734921550 | | | | | Comment bị cắt ("また、") — kiểm tra lại full content trên Backlog |

---

# 親課題: [POS_UI-135] 見積書未印刷一覧(配送端末)

---

## [POS_UI-189] C000132_フリー入力
- 親課題: [POS_UI-135] 見積書未印刷一覧(配送端末)
- Người phụ trách: VTI アイン
- Status: 20_確認待ち
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734925759 | | | | | |
| 2 | Screen Flow & Luồng Xử lý | Áp dụng cùng sửa đổi với POS_UI-164#comment-734921550 (xem comment gốc trên Backlog) | c-734925759 | | | | | Nội dung phụ thuộc POS_UI-164 |
