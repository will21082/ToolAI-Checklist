# SHARP POS UI — Design Review Checklist
> VTI ゴク · 30_差戻／修正依頼 + 20_確認待ち · 2026-05-24 · Chuẩn: Checklist_Screen_Design_VN.md

| | |
|---|---|
| Tổng tickets | 40 |
| Tổng việc cần sửa | 112 |
| Khoảng ngày comment | 2026-03-09 ～ 2026-05-13 |
| Điều kiện lọc | assignee = VTI ゴク · status = 30_差戻／修正依頼, 20_確認待ち · assigneeId=2220256 |

**Cách dùng:** Sửa xong từng dòng → check ✓ Round 1 → khi tất cả xong → upload → đổi status Backlog `40_対応済み／確認依頼`.

---

# 親課題: [POS_UI-4] 入金配送完了

---

## [POS_UI-18] B0210_決済額入力
- 親課題: [POS_UI-4] 入金配送完了
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-10 ～ 2026-04-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Layout & Size — Field | Rút ngắn textbox nhập tiền — 10 chữ số là đủ | | | | | |
| 2 | Component Behavior — Popup | Thêm icon cho từng loại quyết toán (決済種別ごとのアイコン) theo đúng mock | | | | | Khách đã yêu cầu, mock đã có mẫu |
| 3 | Header — Tên màn hình | Hiển thị 売上店・売上伝票 trong header của màn này giống như màn hiện hành | | | | | |
| 4 | Layout & Size — Field | Điều chỉnh layout vùng hiển thị tên 決済種別 để chứa đủ tối đa 10 ký tự toàn giác (vd「ギフト券（釣り銭有）」) | | | | | Tên dài nhất trong master: "ギフト券（釣り銭有）" — 10 ký tự |

---

## [POS_UI-52] B0209_決済（決済種別選択）
- 親課題: [POS_UI-4] 入金配送完了
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-10 ～ 2026-04-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Layout & Size — Field | Rút ngắn textbox nhập tiền — 10 chữ số là đủ | | | | | Áp dụng cùng POS_UI-18#1 |
| 2 | Component Behavior — Popup | Thêm icon cho từng loại quyết toán theo mock | | | | | Áp dụng cùng POS_UI-18#2 |
| 3 | Header — Tên màn hình | Hiển thị 売上店・売上伝票 trong header | | | | | Áp dụng cùng POS_UI-18#3 |
| 4 | Layout & Size — Field | Điều chỉnh layout vùng tên 決済種別 chứa đủ tối đa 10 ký tự toàn giác | | | | | Áp dụng cùng POS_UI-18#4 |

---

# 親課題: [POS_UI-5] 売上返品・売上内容変更

---

## [POS_UI-61] C000040_伝票番号入力
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-18 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Layout & Size — Popup | Phóng to popup — tận dụng khoảng trống màn hình để tăng kích thước, cải thiện thao tác | | | | | Khách phàn nàn chữ nhỏ khó thao tác |
| 2 | Header — Tên màn hình | Đổi tên label 「仕入店」 thành 「売上店」 — tránh gây hiểu nhầm | | | | | Tham chiếu POS_UI-8#comment-712252676 |

---

## [POS_UI-62] C000041_返品のみ／再売上あり選択
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Thay icon「商品明細」bằng icon trực quan hơn — tạo phương án icon mới | | | | | Icon hiện tại không trực quan; SMJ đề xuất tham khảo hình ảnh đính kèm |

---

## [POS_UI-63] C000042_あんしんパスポート（入力待ち）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Table | Áp dụng sửa đổi camera icon và nút tìm kiếm theo POS_UI-58#comment-697967596 | | | | | Xem comment gốc trên Backlog để lấy spec chi tiết |
| 2 | Component Behavior — Popup | Áp dụng sửa đổi popup「あんしんパスポート読込」theo POS_UI-91#comment-700805998 | | | | | |
| 3 | Component Behavior — Popup | Thêm chức năng hiển thị「会員検索サブフォーム」vào design — hiện tại chưa có cách mở form này | | | | | Tham chiếu プログラム仕様書(Ks12000I)：2画面遷移図 |

---

## [POS_UI-64] A0405_決済画面（お買上げ総額入力）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Visual Style — Tab | Đổi cách chuyển đổi giữa 明細情報 và 配送情報 từ button sang tab — thống nhất với màn 配送情報変更 (POS_UI-23) | | | | | |

---

## [POS_UI-65] C000043_商品明細
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Table | Áp dụng sửa đổi camera icon và nút tìm kiếm theo POS_UI-58#comment-697967596 | | | | | |
| 2 | Visual Style — Tab | Đổi design tab giống màn POS_UI-35 | | | | | |
| 3 | Component Behavior — Table | Thêm nút「・・・」để chỉ định phương thức tìm kiếm khác (型番検索 etc.) | | | | | |
| 4 | Layout & Size — Field | Mở rộng textbox JAN — cần chứa đủ 13 chữ số và không bị cắt khi hiển thị | | | | | |

---

## [POS_UI-67] C000045_配送工事区分
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Áp dụng sửa đổi ① từ POS_UI-21#comment-700709542 | | | | | Xem comment gốc để lấy chi tiết |
| 2 | Visual Style — Tab | Đổi design tab giống màn POS_UI-35, và thống nhất toàn bộ design với POS_UI-21 (配送情報変更) | | | | | |

---

## [POS_UI-70] C000050_配送情報選択
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Table | Thống nhất design với POS_UI-111 (B01XX_配送情報選択) — hai màn này là cùng loại | | | | | |

---

## [POS_UI-71] C000051_工事配送案内
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Footer — Stepbar | Đổi tên flow trong footer thành「工事配送案内」(tên màn hình) thay vì「工事情報」 | | | | | Cần xác nhận tối đa bao nhiêu ký tự toàn giác vừa trong step bar |
| 2 | Component Behavior — Popup | Áp dụng sửa đổi từ POS_UI-39#comment-722109099 | | | | | Xem comment gốc trên Backlog |

---

## [POS_UI-74] C000054_設置環境（分類選択）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Visual Style — Tab | Đổi design tab giống màn POS_UI-35 | | | | | |
| 2 | Header — Tên màn hình | Đổi label vùng tiêu đề thành「設置環境:分類選択一覧」 | | | | | |

---

## [POS_UI-75] C000055_設置環境（設問回答選択）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 20_確認待ち
- Ngày comment: 2026-03-16 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Xác nhận với SMJ chức năng nút「次の文」— nếu là thao tác riêng biệt với「確認」thì thiết kế 2 button riêng biệt | | | | | SMJ hỏi để xác nhận flow |
| 2 | Layout & Size — Field | Bố trí vùng chọn câu trả lời (右側エリア) đủ chỗ cho tối đa 10 nút; thiết kế thêm pagination nếu cần ≥9 nút | | | | | Master hiện tại cho phép tối đa 10 câu trả lời |

---

## [POS_UI-76] C000056_設置環境（回答結果確認）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Thiết kế flow khi tap「修正」→ quay về màn chọn câu trả lời của câu hỏi tương ứng (tap vào hàng muốn sửa) | | | | | SMJ gợi ý: tap vào hàng trong bảng kết quả → về câu hỏi đó |
| 2 | Header — Tên màn hình | Đổi toàn bộ「質問」thành「設問」trong màn này | | | | | |

---

## [POS_UI-77] C000057_設置環境（備考）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Áp dụng cùng sửa đổi với POS_UI-47 (C000153_備考入力) — xem comment POS_UI-47#comment-702239402 và #comment-721889899 | | | | | Nội dung cụ thể xem trên Backlog |

---

## [POS_UI-78] C000054_設置環境（設定済み）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Visual Style — Tab | Đổi design tab giống màn POS_UI-35 | | | | | |
| 2 | Header — Tên màn hình | Đổi label vùng tiêu đề thành「設置環境:設定済一覧」 | | | | | |

---

## [POS_UI-79] A0423_元伝の決済入力
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Table | Xóa danh sách button 決済種別 ở bên trái — màn này chỉ nhập số tiền, không chọn loại quyết toán | | | | | |

---

## [POS_UI-80] A0424_新黒伝決済（決済種別選択）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Table | Đồng bộ cấu trúc màn hình với POS_UI-52 (B0209_決済（決済種別選択）) | | | | | |

---

## [POS_UI-81] A0425_新黒伝決済（決済額入力）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Table | Đồng bộ cấu trúc màn hình với POS_UI-18 (B0210_決済額入力) — áp dụng toàn bộ các sửa đổi đã có ở POS_UI-18 | | | | | |

---

## [POS_UI-83] A0427_決済（確定待ち）
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-18 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Layout & Size — Field | Căn chỉnh vị trí số tiền「おつり」thẳng hàng với「お支払金額」「お預かり金額」「残高」 | | | | | |

---

## [POS_UI-117] ヘッダに表示される情報についての確認
- 親課題: [POS_UI-5] 売上返品・売上内容変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-23 ～ 2026-04-24 (SMJ 河野, SMJ 伊藤)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Header — Thông tin nhân viên, hội viên | Thêm các mục ★ vào header 【返品のみ】: ③元販売担当者, ⑦お買上げ総数, ⑧お買上げ総額 | | | | | Hiển thị họ tên kanji (漢字名のみ) |
| 2 | Header — Tên màn hình | Thêm các mục ★ vào header 【再売上あり】: ⑤販売方法, ⑥配送店(受取店/発送店tùy 販売方法) | | | | | 配送店ラベルは販売方法に応じて切り替え |
| 3 | Header — Thông tin nhân viên, hội viên | Bố cục header 2 dòng: dòng 1 (レジ担当者・販売担当者・会員情報), dòng 2 (元伝票番号・販売方法/配送店・お買上げ総数・お買上げ総額) | | | | | |
| 4 | Visual Style — Tab | Xóa shadow cho vùng hiển thị「お買上げ総数」「お買上げ総額」— shadow làm chúng trông như button có thể bấm | | | | | |
| 5 | Visual Style — Tab | Thay background đen cho vùng số tiền bằng màu tương thích với tổng thể header, hoặc tô màu phía label thay vì phía value | | | | | Tham khảo design cuối cùng được chọn từ SMJ 伊藤 2026-04-24 |
| 6 | Visual Style — Tab | Áp dụng design「お買上げ総数」「お買上げ総額」(pattern 2026-04-24) cho tất cả màn hình có hiển thị các thông tin này | | | | | Pattern cuối: xem hình đính kèm SMJ 伊藤 2026-04-24 |

---

# 親課題: [POS_UI-6] 振替出金

---

## [POS_UI-86] C000437_用途選択
- 親課題: [POS_UI-6] 振替出金
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-11 ～ 2026-04-27 (SMJ 河野, SMJ 伊藤)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — List data | Hiển thị toàn bộ 4 menu ngay từ đầu — không ẩn/cần chọn trước | | | | | |
| 2 | Header — Tên màn hình | Đổi tên menu theo danh sách cuối cùng: 「レジにお金を入れる」「レジからお金を出す」「金庫にお金を入れる」「金庫からお金を出す」 | | | | | Tên cuối do SMJ 伊藤 xác nhận 2026-04-27; 振替出金取消 tạm hoãn chờ xác nhận khách hàng |
| 3 | Header — Tên màn hình | Xóa các số thứ tự ①②③ trước tên menu | | | | | |

---

# 親課題: [POS_UI-7] 配送情報変更

---

## [POS_UI-25] C000139_売上伝票番号情報表示-3
- 親課題: [POS_UI-7] 配送情報変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-10 ～ 2026-04-01 (SMJ 河野, SMJ 伊藤)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — List data | Xóa hiển thị「0件」khi không có kết quả | | | | | |
| 2 | Visual Style — Tab | Tăng font size số tiền「お買上げ総数」「お買上げ総額」「売上時残金」lên 20pt | | | | | |
| 3 | Visual Style — Tab | Xóa tab「配送情報」— tab này không còn cần thiết | | | | | |
| 4 | Visual Style — Tab | Xóa tab「決済情報」và xóa màn hình 決済情報 đã tạo — thông tin này xem từ 売上照会 | | | | | |
| 5 | Component Behavior — Popup | Áp dụng sửa đổi từ POS_UI-24#comment-712320326 | | | | | Xem comment gốc trên Backlog |

---

## [POS_UI-26] C000139_売上伝票番号情報表示-5
- 親課題: [POS_UI-7] 配送情報変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-10 ～ 2026-04-01 (SMJ 河野, SMJ 伊藤)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Visual Style — Tab | Đổi UI hiển thị明細 sang dạng card (カード式UI) theo mock 売上 | | | | | |
| 2 | Component Behavior — Popup | Xóa nút「×」— màn này không cho sửa/xóa明細 | | | | | |
| 3 | Visual Style — Tab | Đổi màu toàn bộ hàng明細 và icon sang màu xám (グレー) — không cho chọn/thao tác | | | | | |
| 4 | Visual Style — Tab | Xóa tab「明細情報」và màn hình明細情報 — thông tin này xem từ 売上照会 | | | | | |

---

## [POS_UI-33] C000140_配送情報変更選択-1
- 親課題: [POS_UI-7] 配送情報変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-09 ～ 2026-04-16 (SMJ 伊藤, SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Chuyển nút「閉じる」sang vị trí ngoài cùng bên trái | | | | | |
| 2 | Component Behavior — Popup | Chuyển toggle「添付票要」sang góc trên bên phải | | | | | |
| 3 | Component Behavior — Popup | Cải thiện toggle「添付票要」— làm rõ trạng thái ON/OFF: tăng độ đậm chữ khi ON, hoặc đổi sang dạng button khác | | | | | Tránh nhầm với button thường; SMJ 伊藤 confirm trong Figma chưa rõ |
| 4 | Header — Tên màn hình | Đổi label「編集済み」thành「変更済み」 | | | | | Khách hàng yêu cầu ngày 2026-04-01 |
| 5 | Component Behavior — Popup | Xóa phần「～の変更」trong tên các nút (ví dụ: 「配送予定日の変更」→「配送予定日」) | | | | | Danh sách sau khi xóa: 配送予定日、工事案内、お客様情報、設置環境、配送情報、別紙案内、別配送先、訪問時ご連絡先 |
| 6 | Visual Style — Tab | Xóa tab「決済情報」và tab「明細情報」 | | | | | |

---

## [POS_UI-39] C000147_工事配送案内-1
- 親課題: [POS_UI-7] 配送情報変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-13 ～ 2026-04-16 (SMJ 河野, SMJ 伊藤)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — List data | Thêm hiển thị số lượng (件数) công việc đã thêm vào | | | | | |
| 2 | Component Behavior — Popup | Thêm chức năng chọn bằng nhập số (ナンバー入力) — hiển thị bàn phím số tại vùng đã xác định | | | | | Vị trí bàn phím: xem POS_UI-39#comment-712410000; design bàn phím theo mock 決済画面 |
| 3 | Component Behavior — List data | Giữ lại item đã chọn trong danh sách bên trái (工事配送案内) — không xóa sau khi chuyển sang 選択済み | | | | | |
| 4 | Component Behavior — Popup | Dùng icon「×」để xóa item khỏi 選択済み (xem POS_UI-39#comment-712376061) | | | | | |
| 5 | Component Behavior — Popup | Thiết kế popup thông báo「選択された内容です」khi nhập số vào vùng 選択済み nhầm | | | | | |

---

## [POS_UI-40] C000149_お客様情報
- 親課題: [POS_UI-7] 配送情報変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-04-16 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — List data | Thêm hiển thị số lượng (件数) thông tin khách hàng đã nhập | | | | | |
| 2 | Component Behavior — Popup | Áp dụng cùng sửa đổi với POS_UI-41 (C000148_別紙案内)#comment-712625423 | | | | | Xem comment gốc trên Backlog |
| 3 | Component Behavior — Popup | Thiết kế màn hình chỉnh sửa (編集中) hiện ra sau khi tap icon bút chì (鉛筆マーク) | | | | | |

---

## [POS_UI-41] C000148_別紙案内
- 親課題: [POS_UI-7] 配送情報変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — List data | Thêm hiển thị số lượng (件数) 別紙案内 đã nhập | | | | | |
| 2 | Component Behavior — Popup | Thiết kế màn hình sau khi đã nhập dữ liệu (入力済み) — có xóa hàng và sắp xếp lại (chỉ cho hàng đã chọn) | | | | | Tham chiếu hình POS_UI-41#comment-712625423 và POS_UI-72 |
| 3 | Component Behavior — Popup | Thiết kế màn hình chỉnh sửa (編集中) sau khi tap icon bút chì | | | | | |
| 4 | Component Behavior — Popup | Áp dụng sửa đổi từ POS_UI-162#comment-736182674 | | | | | Xem comment gốc trên Backlog |

---

## [POS_UI-47] C000153_備考入力
- 親課題: [POS_UI-7] 配送情報変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-16 ～ 2026-04-16 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — List data | Thêm hiển thị số lượng (件数) 備考 đã nhập | | | | | |
| 2 | Component Behavior — Popup | Thiết kế trạng thái đã nhập đủ 3 dòng (入力済み 3行) — đây là giới hạn tối đa | | | | | |

---

## [POS_UI-111] B01XX_配送情報選択
- 親課題: [POS_UI-7] 配送情報変更
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-03-13 ～ 2026-04-01 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Áp dụng các sửa đổi từ POS_UI-39 (3 comment: #712374321, #712376061, #712407762) | | | | | Xem comment gốc trên Backlog; nội dung tương tự 工事配送案内 |

---

# 親課題: [POS_UI-132] 見積書

---

## [POS_UI-141] C000094_見積検索サブフォーム
- 親課題: [POS_UI-132] 見積書
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-07 ～ 2026-05-13 (SMJ 河野, SMJ 伊藤)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Table | Thêm camera icon vào bên phải icon kính lúp trong field 見積書番号 | | | | | |
| 2 | Component Behavior — Table | Thêm các field tìm kiếm bổ sung: 電話番号, 顧客コード, カナ氏名 (giống chức năng tìm kiếm của app hiện hành) | | | | | |
| 3 | Component Behavior — Table | Đổi design bảng kết quả giống các màn khác trong hệ thống | | | | | |
| 4 | Component Behavior — Table | Xóa field「No」(ô nhập) — không cần thiết | | | | | |
| 5 | Component Behavior — List data | Sửa label field tìm kiếm thành「顧客コード」(hoặc「会員番号」) — đồng bộ với app hiện hành; xóa icon kính lúp trong field, thay bằng nút「検索」; chuyển nút 検索 và「○件表示」lên phía trên để tăng diện tích hiển thị bảng | | | | | |

---

## [POS_UI-144] C000097_顧客入力
- 親課題: [POS_UI-132] 見積書
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Visual Style — Tab | Xóa tab「別配送先情報」— menu 見積書 không nhập thông tin địa chỉ giao hàng khác | | | | | |
| 2 | Component Behavior — Popup | Thêm thông báo「この変更は実際の顧客情報には反映されません」(hoặc tương đương) khi chỉnh sửa thông tin khách | | | | | Giống cách hiển thị của app hiện hành; xem hình SMJ 河野 2026-05-07 |

---

## [POS_UI-145] C000098_登録のみ or 印刷の確認
- 親課題: [POS_UI-132] 見積書
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-08 ～ 2026-05-13 (SMJ 河野, SMJ 伊藤)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Thêm toggle button「お客様控えを印刷するか しないか」— luôn hiển thị | | | | | |
| 2 | Component Behavior — Popup | Thêm toggle button「会員番号を記載するか しないか」khi khách là hội viên; hiển thị label「会員番号記載無し」khi không phải hội viên | | | | | Xem hình tham chiếu SMJ 河野 2026-05-08; tham chiếu POS_UI-159 |
| 3 | Layout & Size — Field | Giảm kích thước nút「しない」「する」— khoảng cách hiện tại quá hẹp, dễ bấm nhầm | | | | | |
| 4 | Component Behavior — Popup | Đổi nút「閉じる」thành「戻る」; căn khoảng cách「しない」～「戻る」đồng đều | | | | | |
| 5 | Header — Tên màn hình | Thêm mô tả nút「戻る」vào phần giải thích của popup | | | | | |

---

# 親課題: [POS_UI-133] 請求書・納品書印刷

---

## [POS_UI-146] C000100_売上伝票情報、請求書番号入力
- 親課題: [POS_UI-133] 請求書・納品書印刷
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Header — Tên màn hình | Đổi label「変更する」thành「請求書を印刷する」 | | | | | |
| 2 | Header — Tên màn hình | Đổi label「請求書情報」thành「納品書を印刷する」 | | | | | |
| 3 | Header — Tên màn hình | Đổi label vùng thông tin khác thành「～情報」(xem hình SMJ 河野 2026-05-07) | | | | | |
| 4 | Component Behavior — Popup | Xóa vùng hiển thị 売上店・売上店名 — thông tin này không cần thiết ở màn này | | | | | |

---

## [POS_UI-147] C000102 伝票検索サブフォーム
- 親課題: [POS_UI-133] 請求書・納品書印刷
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Data Format — Số tiền | Sửa field 売上日 (năm) từ 5 chữ số về 4 chữ số | | | | | |
| 2 | Header — Tên màn hình | Đổi label「顧請求書番号客氏名」thành「請求書番号」 | | | | | Lỗi typo trong label hiện tại |
| 3 | Component Behavior — Table | Thêm field tìm kiếm: 顧客コード, カナ氏名 (ngoài 電話番号 đã có) | | | | | |
| 4 | Component Behavior — Popup | Hiển thị「済」trong cột 請求書発行・納品書発行 khi đã phát hành | | | | | |

---

## [POS_UI-152] C000107_印刷確認
- 親課題: [POS_UI-133] 請求書・納品書印刷
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-08 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Visual Style — Tab | Sửa design message về đúng design 現行 (hiện tại đang dùng design của màn 見積書) | | | | | Xem hình tham chiếu SMJ 河野 2026-05-08 |

---

## [POS_UI-153] C000108_納品書印刷確認
- 親課題: [POS_UI-133] 請求書・納品書印刷
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-08 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Đổi「販売担当者」thành「印刷担当者」trong màn này | | | | | |
| 2 | Component Behavior — Popup | Sửa title và màn hình nguồn (表示元) từ「請求書印刷」sang「納品書印刷」— hiển thị trên vùng 明細画面 | | | | | Xem hình tham chiếu SMJ 河野 2026-05-08 |

---

# 親課題: [POS_UI-134] 見積書未承認一覧(配送端末)

---

## [POS_UI-154] C000109_担当者入力（レジ入力者／販売担当者）
- 親課題: [POS_UI-134] 見積書未承認一覧(配送端末)
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Popup | Đổi「自店担当者」thành「入力担当者」— đồng bộ với app hiện hành | | | | | |

---

## [POS_UI-156] C000112_端末見積書検索サブフォーム
- 親課題: [POS_UI-134] 見積書未承認一覧(配送端末)
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-07 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Component Behavior — Table | Thêm camera icon bên phải icon kính lúp trong field 見積書番号 — theo design POS_UI-141 (xem hình SMJ 河野 2026-05-13) | | | | | |
| 2 | Component Behavior — Table | Thêm field tìm kiếm: 電話番号, 顧客コード, カナ氏名; dùng data tối đa từng cột | | | | | |
| 3 | Component Behavior — Table | Điều chỉnh tên cột và layout giống với màn 見積検索サブフォーム (POS_UI-141) nhưng nội dung phù hợp với 端末見積書 | | | | | |

---

## [POS_UI-159] C000113_印刷確認
- 親課題: [POS_UI-134] 見積書未承認一覧(配送端末)
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-08 ～ 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Visual Style — Tab | Giữ nguyên design message hiện tại (đã xác nhận là phù hợp) | | | | | SMJ 河野 xác nhận 2026-05-12: message đúng, chỉ cần sửa text |
| 2 | Header — Tên màn hình | Đổi label「お客様控えのみ」thành「お客様控えのみを印刷」 | | | | | |
| 3 | Header — Tên màn hình | Đổi label「会員番号記載」thành「見積書に会員番号を記載」 | | | | | |

---

# 親課題: [POS_UI-135] 見積書未印刷一覧(配送端末)

---

## [POS_UI-179] C000122_担当者入力（レジ入力者／販売担当者）
- 親課題: [POS_UI-135] 見積書未印刷一覧(配送端末)
- Người phụ trách: VTI ゴク
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-07 (SMJ 河野)

| # | Nhóm | Việc cần sửa | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|---------|---------|---------|---|--------|
| 1 | Header — Tên màn hình | Đổi title màn hình thành「見積書未印刷一覧（配送端末）」 | | | | | |
| 2 | Component Behavior — Popup | Đổi「自店担当者」thành「印刷担当者」— đồng bộ với app hiện hành | | | | | |
