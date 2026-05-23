# SHARP POS UI — Checklist 差戻／修正依頼

| Mục | Giá trị |
|---|---|
| Project | POS_UI — siconnect.backlog.com |
| Assignee | VTI アイン |
| Status lọc | 30_差戻／修正依頼 |
| Tổng tickets nguồn | 45 |
| Ngày tổng hợp | 2026-05-24 |
| Người tổng hợp | VTI アイン |

---

## Tổng kết Round

| Round | OK | NOK | N/A | Kết quả |
|---|---|---|---|---|
| Round 1 | | | | Pass / Review Again / Acceptable |
| Round 2 | | | | Pass / Review Again / Acceptable |
| Round 3 | | | | Pass / Review Again / Acceptable |

---

## Checklist Chi tiết

| # | Phân loại / Nhóm | Flow / Screen | Check Item (Rule) | 出典 | Mandatory | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|---|---|
| **1** | **Header & Navigation** | | | | | | | | |
| 1.1 | Header & Navigation | C000123/124/125/126/127/128/129/130/131/133/134 | Tiêu đề màn hình có được đổi thành「見積書未印刷一覧（配送端末）」không? | POS_UI-180,181,182,184,185,186,187,188,190,191 | M | | | | Áp dụng đồng loạt toàn bộ nhóm màn 見積書未印刷 |
| 1.2 | Header & Navigation | C000180_指定方法選択 | Từ「指定方法」chỉ xuất hiện 1 lần trong tiêu đề; guide「～を選択してください」và vùng xanh lá「検索方法」có được xóa không? | POS_UI-174 | | | | | |
| 1.3 | Header & Navigation | C000123_検索方法選択 | Từ「検索方法」chỉ xuất hiện 1 lần; guide trùng lặp có được xóa, vùng xanh sửa thành text「検索方法選択」, nút「指定なし」→「指定せずに検索」không? | POS_UI-180 | | | | | |
| 1.4 | Header & Navigation | 元伝決済時カード持ち確認 | Tiêu đề「元伝決済時カード」ở phía trên màn hình có được xóa không? | POS_UI-198 | M | | | | |
| 1.5 | Header & Navigation | 元伝カード決済引き継ぎの確認 | Tiêu đề「元伝カード決済」ở phía trên màn hình có được xóa không? | POS_UI-197 | M | | | | |
| 1.6 | Header & Navigation | C000103/C000104 | Footer progress bar không cần thiết có được xóa khỏi màn hình in不? | POS_UI-148,149 | | | | | |
| 1.7 | Header & Navigation | C000178_配送工事区分選択 | Guide message có được cập nhật nội dung phù hợp với màn hình hiện tại (không dùng guide của 予約担当者入力) không? | POS_UI-173 | | | | | |
| **2** | **UI Components & Controls** | | | | | | | | |
| 2.1 | UI Components & Controls | C000048/C000047/C000178 | Thiết kế button thời gian (時間帯) có được đồng bộ theo chuẩn màn 配送情報変更_時間帯選択 không? | POS_UI-69,173,201 | M | | | | Áp dụng đồng loạt mọi màn có 時間帯 |
| 2.2 | UI Components & Controls | C000180/C000123 | Kích thước button「閉じる」có được thu nhỏ khớp với các màn hình khác (không cùng cỡ button chính khiến trông như 3 lựa chọn) không? | POS_UI-174,180 | | | | | |
| 2.3 | UI Components & Controls | C000181/C000182/B0401 | Button không cần dùng (「確定」ボタン不要, 「特定エリア表示」削除) có được xóa không? | POS_UI-175,176,178 | | | | | |
| 2.4 | UI Components & Controls | B0401エリア絞込 | Tên button「進む」có được đổi thành「確定」không? | POS_UI-175 | M | | | | |
| 2.5 | UI Components & Controls | C000185_明細入力 | Tên button「取消」có được đổi thành「在庫予約を取消」không? | POS_UI-167 | M | | | | |
| 2.6 | UI Components & Controls | C000181/C000182 | Button「印刷」có được tô màu xanh (青いボタン) không? | POS_UI-176,178 | | | | | |
| 2.7 | UI Components & Controls | C000178_配送工事区分選択 | Thiết kế màn hình khi keyboard hiển thị (入力時) có được tạo không? | POS_UI-173 | | | | | |
| 2.8 | UI Components & Controls | C000178_配送工事区分選択 | Khi số lượng thời gian = 0, hiển thị「0/10」và button ở trạng thái 非活性 (không thể nhấn) có được thiết kế không? | POS_UI-173 | | | | | |
| 2.9 | UI Components & Controls | C000103/C000104 | Checkbox「予定日未定」(không cần vì ngày luôn xác định khi phát hành hóa đơn) có được xóa không? | POS_UI-148,149 | M | | | | |
| 2.10 | UI Components & Controls | C000124_未印刷一覧表示 | Header cột "選択" có dùng label text「選択」thay vì checkbox control không? | POS_UI-182 | | | | | |
| 2.11 | UI Components & Controls | B0401/C000181/C000182/C000124 | Scrollbar có được điều chỉnh không đè lên vùng dữ liệu (明細・金額欄) không? | POS_UI-175,176,178,182 | | | | | |
| **3** | **Hiển thị & Đồng bộ Thông tin** | | | | | | | | |
| 3.1 | Hiển thị & Đồng bộ | 元伝と新黒決済確認 | お買上げ総数・総額が最新デザインに反映されているか? (画像赤枠) | POS_UI-195 | M | | | | |
| 3.2 | Hiển thị & Đồng bộ | 元伝と新黒決済確認 | 未決済金額がデザインに反映されているか? (画像青枠) | POS_UI-195 | M | | | | |
| 3.3 | Hiển thị & Đồng bộ | C000176_空き状況一覧表示 | Vùng「センター店」chỉ hiển thị 店舗名 (không hiển thị 法人-店舗コード vì đã có ở vùng trái) không? | POS_UI-171 | M | | | | |
| 3.4 | Hiển thị & Đồng bộ | C000176_空き状況一覧表示 | Độ rộng hiển thị 店舗名 có tính đến tối đa 全角16文字 không? Dữ liệu mẫu có dùng chuỗi tối đa không? | POS_UI-171 | | | | | |
| 3.5 | Hiển thị & Đồng bộ | C000114/C000127_詳細 | Khi khách hàng không phải hội viên あんしんパスポート, màn hình có hiển thị thông báo tương ứng không? | POS_UI-158,183 | M | | | | Giữ nguyên spec hiện hành |
| 3.6 | Hiển thị & Đồng bộ | C000186_在庫引当確認 | Câu「DC在庫の引当を行いますか。」có font size đủ lớn và nổi bật không? Tiêu đề trùng nội dung có được xóa không? | POS_UI-169 | | | | | |
| 3.7 | Hiển thị & Đồng bộ | C000186_在庫引当確認 | Lựa chọn có được đổi thành「いいえ」「はい」không? | POS_UI-169 | M | | | | |
| 3.8 | Hiển thị & Đồng bộ | C000181/C000182 | Thiết kế cả 2 trạng thái: đã nhập (入力済み) và chưa nhập (未入力) đều có không? | POS_UI-176,178 | M | | | | |
| 3.9 | Hiển thị & Đồng bộ | B0401/C000181/C000182/C000124 | Dữ liệu mẫu trong từng dòng có nội dung khác nhau (không lặp cùng một data) không? | POS_UI-175,176,178,182 | | | | | |
| 3.10 | Hiển thị & Đồng bộ | C000181/C000182 | Địa chỉ hiển thị「都道府県＋市」thay vì「ミトミツクニ」không? | POS_UI-176,178 | M | | | | |
| 3.11 | Hiển thị & Đồng bộ | C000176_空き状況一覧表示 | Chức năng 前週/今週/翌週 đã phản ánh đúng spec: 今週 thì 前週 không chuyển được; 翌週 có thể xem đến hơn 1 năm tới không? | POS_UI-171 | | | | | |
| 3.12 | Hiển thị & Đồng bộ | C000176_空き状況一覧表示 | Lỗi chính tả「アリア」có được sửa thành「エリア」không? | POS_UI-171 | M | | | | |
| 3.13 | Hiển thị & Đồng bộ | C000181/C000182 | Lỗi chữ Hán trong「頻度」có được sửa đúng không? | POS_UI-176,178 | M | | | | |
| 3.14 | Hiển thị & Đồng bộ | C000185_明細入力 | Thiết kế trường hợp không có tồn kho (在庫なし, No1 display) có được tạo không? | POS_UI-167 | | | | | |
| 3.15 | Hiển thị & Đồng bộ | C000101_請求書一覧 | Màn hình明細 in hóa đơn có được thêm vào Figma 画面遷移図 không? | POS_UI-140 | | | | | |
| 3.16 | Hiển thị & Đồng bộ | C000183/C000176 | Ticket POS_UI-203 có được xác nhận trùng với POS_UI-171 và xử lý (đóng hoặc hợp nhất) không? | POS_UI-203 | | | | | Cần confirm với PM |
| **4** | **Cấu trúc Layout & Vị trí Thông tin** | | | | | | | | |
| 4.1 | Layout & Vị trí | B0401/C000181/C000182 | Data dạng code (エリアコード, JISコード, 配送頻度) có căn giữa (中央揃え) không? | POS_UI-175,176,178 | M | | | | Chuẩn: code → center, text → left |
| 4.2 | Layout & Vị trí | B0401エリア絞込 | Độ rộng cột エリア名称 có đủ cho tối đa 全角30文字 với margin thoải mái không? Kích thước subform có được điều chỉnh không? | POS_UI-175 | | | | | |
| 4.3 | Layout & Vị trí | C000185_明細入力 | Hiển thị明細 có dùng dạng card (カード形式) giống màn hình 売上, không dùng bảng (表形式) không? | POS_UI-167 | M | | | | |
| 4.4 | Layout & Vị trí | C000185_明細入力 | Tối đa 3明細 / 1 giao dịch có đủ không gian hiển thị không? | POS_UI-167 | M | | | | |
| 4.5 | Layout & Vị trí | C000103/C000104/C000105 | Nhãn「販売担当者」có được đổi thành「印刷担当者」không? | POS_UI-148,149,150 | M | | | | |
| 4.6 | Layout & Vị trí | C000103/C000104 | Văn bản trong khung【請求書　印刷サンプル】có gói gọn trong 1 dòng không? Tên khung【法求出...】có được sửa thành【請求書　印刷サンプル】không? | POS_UI-148,149 | | | | | |
| 4.7 | Layout & Vị trí | C000104_お支払予定日 | Label「お支払予定日」chỉ hiển thị 1 lần không? | POS_UI-149 | | | | | |
| 4.8 | Layout & Vị trí | C000103_請求書日付 | Label「元伝の決済」không cần thiết có được xóa không? | POS_UI-148 | | | | | |
| 4.9 | Layout & Vị trí | C000185_明細入力 | Button「在庫予約を取消」(戻る系) có được đặt ở bên trái không? | POS_UI-167 | | | | | |
| 4.10 | Layout & Vị trí | C000126_印刷確認 | Text button đã đổi thành「お客様控えのみを印刷」và「見積書に会員番号を記載」chưa? | POS_UI-184 | M | | | | Từ cũ ngắn quá, không trực quan |
| 4.11 | Layout & Vị trí | C000178_配送工事区分選択 | Vùng「エリア」hiển thị tên khu vực giao hàng/công trình (水戸, いわき, ...) không phải 店舗コード/店舗名 không? | POS_UI-173 | M | | | | |
| **5** | **Screen Flow & Luồng Xử lý** | | | | | | | | |
| 5.1 | Screen Flow | 元伝決済時カード持ち確認 | Sau khi chọn「元伝決済時カード」luồng có chuyển màn tự động không, hay cần thêm button xác nhận? (cần confirm với khách trước khi thiết kế) | POS_UI-198 | | | | | Chờ confirm spec từ khách |
| 5.2 | Screen Flow | C000101_請求書・納品書 | Màn hình in có được thiết kế theo hướng 商品明細 không thể thêm/xóa/sửa (read-only) không? | POS_UI-140 | M | | | | |
| 5.3 | Screen Flow | C000181/C000182 | Màn hình sau khi nhấn button「宅配不可エリア」có được thiết kế không? | POS_UI-176,178 | | | | | |
| 5.4 | Screen Flow | C000126_印刷確認 | Luồng in từ màn hình「未印刷一覧表示」có phản ánh đúng flow hiện hành của khách không? | POS_UI-184 | | | | | |
| **6** | **Input Fields & Form Design** | | | | | | | | |
| 6.1 | Input Fields | C000106_摘要入力 | Thiết kế có thể hiện đúng spec: 1行全角45文字×5行 với MAX文字数 không? Nếu thừa khoảng trắng có điều chỉnh không? | POS_UI-151 | M | | | | |
| 6.2 | Input Fields | C000185_明細入力 | Chức năng tìm kiếm theo型番 có button hoặc giải pháp khác được thiết kế không? | POS_UI-167 | | | | | |
| 6.3 | Input Fields | C000185/C000182/C000124 | Tooltip có được thiết kế cho các vị trí hiển thị「...」(văn bản bị cắt ngắn) không? | POS_UI-167,182 | | | | | |
| 6.4 | Input Fields | C000123_検索方法選択 | Thiết kế có dùng nền trắng (白背景) cho popup chọn phương thức, không đè lên màn hình担当者 không? | POS_UI-180 | | | | | |
| 6.5 | Input Fields | C000110_検索方法選択 | Các sửa đổi theo comment POS_UI-180 có được áp dụng đồng bộ cho C000110 không? | POS_UI-155 | | | | | C000110 dùng chung spec với C000123 |
| **7** | **Tab & Thông tin Chi tiết / Consistency** | | | | | | | | |
| 7.1 | Tab & Consistency | C000114_詳細 | Màn hình「C000114_詳細」có được thêm đủ các tab:「次回訪問予定」「別紙内容確認」「見積内容」「見積結果」「フリー入力」「店舗への連絡」「コメント」không? | POS_UI-158,160,161,162,163,165,166,183,185,186,187,188,190,191 | M | | | | Áp dụng đồng loạt C000114～C000134 |
| 7.2 | Tab & Consistency | C000124_未印刷一覧表示 | Button xanh trong màn in đã được đặt tên「印刷」chưa? (menu in見積書đã duyệt) | POS_UI-182 | | | | | |
| 7.3 | Tab & Consistency | C000124_未印刷一覧表示 | Các button chức năng (赤枠) từ màn hình cũ đã được thêm lại hoặc có giải pháp thay thế chưa? | POS_UI-182 | | | | | |
| 7.4 | Tab & Consistency | A0426_新黒伝決済（お預かり金額入力） | Thiết kế có được đồng bộ với các menu khác trong cùng hệ thống không? | POS_UI-82 | M | | | | ⚠️ Due: 2026-03-31 |
| 7.5 | Tab & Consistency | C000111_未承認一覧表示 | Yêu cầu thêm button chức năng đang tạm hoãn (保留) — có xác nhận không làm trong round này không? | POS_UI-157 | | | | | Không cần làm, chờ khách confirm vị trí |
| 7.6 | Tab & Consistency | C000053_お客様情報 | Các sửa đổi theo comment gốc POS_UI-40 có được áp dụng không? | POS_UI-73 | | | | | ⚠️ Due: 2026-03-31 — kiểm tra comment POS_UI-40 |

---

Summary: Number of OK / NOK / N/A items (per Round). Review Result: Pass / Review Again / Acceptable.
