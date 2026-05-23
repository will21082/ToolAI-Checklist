# SHARP POS UI — Checklist 差戻 theo từng Ticket

| Mục | Giá trị |
|---|---|
| Project | POS_UI — siconnect.backlog.com |
| Assignee | VTI アイン |
| Status | 30_差戻／修正依頼 |
| Tổng | 45 tickets |
| Ngày | 2026-05-24 |

---

## Hướng dẫn dùng

- **Sửa gì**: đọc phần "Feedback khách" — đây là nguyên văn yêu cầu của khách
- **Check gì**: từng dòng `- [ ]` là 1 điểm cần xác nhận sau khi sửa xong
- Khi hoàn thành 1 ticket → đánh `[x]` vào tất cả checkbox → đổi status Backlog → `20_確認待ち`

---

## ⚠️ Ưu tiên cao (có deadline 2026-03-31)

---

### [POS_UI-82] A0426_新黒伝決済（お預かり金額入力）
**Feedback khách:** Thiết kế khác với các menu khác, cần thống nhất lại.

- [ ] So sánh thiết kế với các màn hình cùng luồng 新黒伝決済 — layout, màu sắc, font, button đã đồng bộ chưa?
- [ ] Upload bản sửa lên Backlog + đổi status → 20_確認待ち

---

### [POS_UI-69] C000048_時間帯選択
**Feedback khách:** Align thiết kế theo màn 配送情報変更_時間帯選択.

- [ ] Thiết kế button 時間帯 đã khớp với màn 配送情報変更_時間帯選択 chưa? (màu, kích thước, trạng thái active/inactive)
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-72] C000052_別紙案内
**Feedback khách:** *(Chưa có comment — cần vào Backlog xem comment gốc)*

- [ ] Xem comment mới nhất trên Backlog để biết yêu cầu cụ thể
- [ ] Thực hiện sửa và upload

---

### [POS_UI-73] C000053_お客様情報
**Feedback khách:** Xem comment tại POS_UI-40.

- [ ] Mở ticket POS_UI-40 đọc comment gốc để biết yêu cầu cụ thể
- [ ] Thực hiện sửa theo comment đó
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

## Nhóm 決済系

---

### [POS_UI-195] 元伝と新黒決済確認
**Feedback khách:**
- お買上げ総数・総額 chưa được cập nhật theo design mới nhất (xem ảnh vùng đỏ)
- 未決済金額 chưa được đưa vào design (xem ảnh vùng xanh)

- [ ] お買上げ総数 và 総額 đã hiển thị theo design mới nhất chưa?
- [ ] 未決済金額 đã được thêm vào design chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-197] 元伝カード決済引き継ぎの確認
**Feedback khách:** Xóa tiêu đề「元伝カード決済」đang hiển thị ở phía trên màn hình.

- [ ] Tiêu đề「元伝カード決済」ở phía trên đã được xóa chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-198] 元伝決済時カード持ち確認
**Feedback khách:**
- Xóa tiêu đề「元伝決済時カード」ở phía trên
- Sau khi chọn「元伝決済時カード」thì chuyển màn tự động hay cần button xác nhận? (cần confirm với khách vì hiện không có button)

- [ ] Tiêu đề「元伝決済時カード」ở phía trên đã được xóa chưa?
- [ ] Đã xác nhận với khách về luồng chuyển màn (tự động hay cần button) chưa? *(cần hỏi trước khi sửa)*
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-194] 返品エラー通知
**Feedback khách:** *(Chưa có comment — cần vào Backlog xem comment gốc)*

- [ ] Xem comment mới nhất trên Backlog để biết yêu cầu cụ thể
- [ ] Thực hiện sửa và upload

---

### [POS_UI-196] C000058_決済種別変更の確認
**Feedback khách:** *(Chưa có comment — cần vào Backlog xem comment gốc)*

- [ ] Xem comment mới nhất trên Backlog để biết yêu cầu cụ thể
- [ ] Thực hiện sửa và upload

---

## Nhóm 請求書・印刷系

---

### [POS_UI-140] C000101_請求書一覧／納品書一覧表示
**Feedback khách:**
- Thêm màn明細 của 請求書印刷 vào Figma 画面遷移図
- Màn in 請求書/納品書: thiết kế theo hướng 商品明細 không thể thêm/xóa/sửa (read-only)

- [ ] Màn明細 in 請求書 đã được thêm vào Figma 画面遷移図 chưa?
- [ ] Thiết kế đã thể hiện rõ 商品明細 là read-only (không có nút thêm/xóa/sửa) chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-148] C000103_請求書日付
**Feedback khách:**
- Đổi「販売担当者」→「印刷担当者」
- Xóa label「元伝の決済」
- Xóa checkbox「予定日未定」(ngày luôn xác định khi phát hành hóa đơn)
- Văn bản trong khung【請求書　印刷サンプル】gói gọn 1 dòng
- Tên khung【法求出 印刷サンプル】→【請求書　印刷サンプル】
- Vị trí văn bản theo ảnh đính kèm
- Xóa footer progress bar

- [ ] Label đã đổi「販売担当者」→「印刷担当者」chưa?
- [ ] Label「元伝の決済」đã được xóa chưa?
- [ ] Checkbox「予定日未定」đã được xóa chưa?
- [ ] Văn bản trong khung in đã gói gọn 1 dòng chưa?
- [ ] Tên khung đã sửa thành【請求書　印刷サンプル】chưa?
- [ ] Vị trí văn bản đã khớp ảnh đính kèm chưa?
- [ ] Footer progress bar đã được xóa chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-149] C000104_お支払予定日
**Feedback khách:**
- Đổi「販売担当者」→「印刷担当者」
- Label「お支払予定日」chỉ hiện 1 lần
- Xóa checkbox「予定日未定」
- Văn bản trong khung【請求書　印刷サンプル】gói gọn 1 dòng
- Tên khung【法求出 印刷サンプル】→【請求書　印刷サンプル】
- Vị trí vùng đỏ và văn bản theo ảnh đính kèm
- Xóa footer progress bar

- [ ] Label đã đổi「販売担当者」→「印刷担当者」chưa?
- [ ] Label「お支払予定日」chỉ còn 1 cái chưa?
- [ ] Checkbox「予定日未定」đã được xóa chưa?
- [ ] Văn bản trong khung đã gói gọn 1 dòng chưa?
- [ ] Tên khung đã sửa thành【請求書　印刷サンプル】chưa?
- [ ] Vị trí đã khớp ảnh đính kèm chưa?
- [ ] Footer progress bar đã được xóa chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-150] C000105_お客様氏名
**Feedback khách:** Đổi「販売担当者」→「印刷担当者」.

- [ ] Label đã đổi「販売担当者」→「印刷担当者」chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-151] C000106_摘要入力
**Feedback khách:** Spec là 1行全角45文字×5行 — cần tạo design với MAX văn bản. Nếu thừa khoảng trắng thì điều chỉnh layout.

- [ ] Textbox đã thể hiện đúng 1行45文字×5行 chưa?
- [ ] Design đã có thêm trường hợp MAX văn bản chưa?
- [ ] Layout đã được điều chỉnh nếu thừa khoảng trắng chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-184] C000126_印刷確認
**Feedback khách:**
- Đổi text button:「お客様控えのみ」→「お客様控えのみを印刷」;「会員番号記載」→「見積書に会員番号を記載」
- Phản ánh đúng flow in hiện hành (xem ảnh đính kèm)

- [ ] Text button đã đổi「お客様控えのみを印刷」chưa?
- [ ] Text button đã đổi「見積書に会員番号を記載」chưa?
- [ ] Flow in đã khớp với ảnh flow hiện hành đính kèm chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

## Nhóm 見積書未印刷系 (C000110～C000134)

> **Lưu ý chung cho cả nhóm này:** Tiêu đề tất cả màn hình trong nhóm phải đổi thành **「見積書未印刷一覧（配送端末）」**

---

### [POS_UI-155] C000110_検索方法選択
**Feedback khách:** Áp dụng các sửa đổi theo comment của POS_UI-180 (C000123 cùng loại màn hình).

- [ ] Đã xem comment POS_UI-180 để biết yêu cầu cụ thể chưa?
- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Các sửa đổi của C000123 đã được áp dụng đồng bộ chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-157] C000111_未承認一覧表示
**Feedback khách:** Yêu cầu thêm button chức năng (vùng đỏ) đang **tạm hoãn** — khách đang xem xét vị trí đặt button.

- [ ] Xác nhận: item này đang bảo lưu, **chưa cần làm** trong round này *(chờ khách confirm)*
- [ ] Các điểm khác trong ticket (nếu có) đã được xử lý chưa?

---

### [POS_UI-158] C000114_詳細
**Feedback khách:** Khi khách hàng không phải hội viên あんしんパスポート thì hiển thị thông báo tương ứng (giống hiện hành — xem ảnh đính kèm).

- [ ] Trường hợp không phải hội viên あんしんパスポート đã được thêm vào design chưa?
- [ ] Nội dung hiển thị đã khớp với ảnh đính kèm chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-160] C000115_別紙内容確認
**Feedback khách:**「C000114_詳細」cần thêm các tab「次回訪問予定」～「コメント」— màn này là 1 trong các tab đó (xem ảnh đính kèm).

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Tab「別紙内容確認」đã được thêm vào màn C000114_詳細 chưa?
- [ ] Nội dung tab đã khớp ảnh đính kèm chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-161] C000116_次回訪問予定
**Feedback khách:**「C000114_詳細」cần thêm các tab「次回訪問予定」～「コメント」.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Tab「次回訪問予定」đã được thêm vào màn C000114_詳細 chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-162] C000117_見積内容
**Feedback khách:**「C000114_詳細」cần thêm các tab「次回訪問予定」～「コメント」.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Tab「見積内容」đã được thêm vào màn C000114_詳細 chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-163] C000118_見積結果
**Feedback khách:**「C000114_詳細」cần thêm các tab「次回訪問予定」～「コメント」.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Tab「見積結果」đã được thêm vào màn C000114_詳細 chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-165] C000120_店舗への連絡
**Feedback khách:**「C000114_詳細」cần thêm các tab「次回訪問予定」～「コメント」.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Tab「店舗への連絡」đã được thêm vào màn C000114_詳細 chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-166] C000121_コメント
**Feedback khách:**「C000114_詳細」cần thêm các tab「次回訪問予定」～「コメント」.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Tab「コメント」đã được thêm vào màn C000114_詳細 chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-180] C000123_検索方法選択
**Feedback khách:**
- Tiêu đề →「見積書未印刷一覧（配送端末）」
- Dùng nền trắng (白背景) cho popup chọn phương thức, không đè lên màn担当者
- Từ「検索方法」chỉ xuất hiện 1 lần — xóa guide「～を選択してください」, sửa vùng xanh thành text「検索方法選択」
- Đổi「指定なし」→「指定せずに検索」
- Button「閉じる」thu nhỏ lại khớp với các màn khác (hiện cùng size với button chính trông như 3 lựa chọn)

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Popup đã dùng nền trắng, không đè lên màn担当者 chưa?
- [ ] Từ「検索方法」chỉ còn 1 lần; guide trùng đã được xóa chưa?
- [ ] Vùng xanh đã sửa thành text「検索方法選択」chưa?
- [ ] Nút「指定なし」đã đổi thành「指定せずに検索」chưa?
- [ ] Kích thước button「閉じる」đã được thu nhỏ cho khớp với các màn khác chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-181] C000125_端末見積書検索サブフォーム
**Feedback khách:**
- Tiêu đề →「見積書未印刷一覧（配送端末）」
- Áp dụng các sửa đổi theo comment POS_UI-156

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Đã xem comment POS_UI-156 để áp dụng yêu cầu cụ thể chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-182] C000124_未承認一覧表示
**Feedback khách:**
- Tên ticket → đổi thành「C000124_未印刷一覧表示」
- Tiêu đề màn →「見積書未印刷一覧（配送端末）」
- Header cột "選択": dùng text「選択」thay vì checkbox control
- Thêm lại các button chức năng (vùng đỏ trong ảnh) hoặc giải pháp thay thế; button xanh đặt tên「印刷」
- Scrollbar không đè lên vùng金額
- Dữ liệu mẫu: mỗi dòng có nội dung khác nhau; thêm tooltip cho chỗ hiển thị「...」

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Header cột "選択" đã dùng text thay vì checkbox control chưa?
- [ ] Các button chức năng (vùng đỏ) đã được thêm lại hoặc có giải pháp thay thế chưa?
- [ ] Button xanh đã đặt tên「印刷」chưa?
- [ ] Scrollbar đã không đè lên vùng金額 chưa?
- [ ] Dữ liệu mẫu mỗi dòng có nội dung khác nhau chưa?
- [ ] Tooltip đã được thêm cho các chỗ hiển thị「...」chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-183] C000127_詳細
**Feedback khách:** Khi khách hàng không phải hội viên あんしんパスポート thì hiển thị thông báo tương ứng (xem ảnh đính kèm).

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Trường hợp không phải hội viên あんしんパスポート đã được thêm vào design chưa?
- [ ] Nội dung hiển thị đã khớp ảnh đính kèm chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-185] C000128_別紙内容確認
**Feedback khách:** Tiêu đề →「見積書未印刷一覧（配送端末）」; áp dụng comment đã có.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Các sửa đổi theo comment đã áp dụng chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-186] C000129_次回訪問予定
**Feedback khách:** Tiêu đề →「見積書未印刷一覧（配送端末）」; áp dụng comment đã có.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Các sửa đổi theo comment đã áp dụng chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-187] C000130_見積内容
**Feedback khách:** Tiêu đề →「見積書未印刷一覧（配送端末）」; áp dụng comment đã có.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Các sửa đổi theo comment đã áp dụng chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-188] C000131_見積結果
**Feedback khách:** Tiêu đề →「見積書未印刷一覧（配送端末）」; áp dụng comment đã có.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Các sửa đổi theo comment đã áp dụng chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-190] C000133_店舗への連絡
**Feedback khách:** Tiêu đề →「見積書未印刷一覧（配送端末）」; áp dụng comment đã có.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Các sửa đổi theo comment đã áp dụng chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-191] C000134_コメント
**Feedback khách:** Tiêu đề →「見積書未印刷一覧（配送端末）」; áp dụng comment đã có tại POS_UI-166.

- [ ] Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa?
- [ ] Các sửa đổi theo comment POS_UI-166 đã áp dụng chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

## Nhóm 配送・予約系

---

### [POS_UI-167] C000185_明細入力
**Feedback khách:**
- Đổi từ bảng (表形式) sang dạng card (カード形式) giống màn 売上 (vì型番quá ngắn)
- 1 giao dịch tối đa 3明細 — cần đủ chỗ hiển thị 3 cái
- Chỗ nào hiển thị「...」thì thêm tooltip
- Thêm button (hoặc giải pháp khác) để tìm kiếm theo型番
- Đổi tên button「取消」→「在庫予約を取消」; đặt sang bên trái (đây là button quay lại)
- Trường hợp không có tồn kho (No1) — cần thêm design cho case này

- [ ] Hiển thị đã đổi sang dạng card (カード形式) chưa?
- [ ] 3明細 có đủ chỗ hiển thị không bị cắt không?
- [ ] Tooltip đã được thêm cho các chỗ hiển thị「...」chưa?
- [ ] Chức năng tìm kiếm theo型番 đã có trong design chưa?
- [ ] Button「取消」đã đổi tên thành「在庫予約を取消」và đặt bên trái chưa?
- [ ] Design trường hợp không có tồn kho đã được tạo chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-169] C000186_在庫引当確認 / 予約取消確認
**Feedback khách:**
- Font size của「DC在庫引当を行いますか。」quá nhỏ, cần phóng to
- Xóa tiêu đề (nội dung trùng với body); sửa body thành「DC在庫の引当を行いますか。」
- Đổi lựa chọn thành「いいえ」「はい」

- [ ] Font size của câu xác nhận đã được phóng to, nổi bật hơn chưa?
- [ ] Tiêu đề trùng lặp đã được xóa chưa?
- [ ] Nội dung body đã sửa thành「DC在庫の引当を行いますか。」chưa?
- [ ] Lựa chọn đã đổi thành「いいえ」「はい」chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-171] C000176_空き状況一覧表示
**Feedback khách:**
- Vùng「センター店」: chỉ hiển thị tên cửa hàng (店舗名のみ), không hiển thị mã vì đã có ở vùng trái
- Độ rộng tên cửa hàng phải tính đến tối đa 全角16文字; dùng dữ liệu mẫu tối đa
- Spec 前週/今週/翌週: đang ở 今週 thì 前週 không chuyển được; 翌週 có thể xem đến hơn 1 năm tới
- Sửa lỗi chính tả「アリア」→「エリア」

- [ ] Vùng「センター店」chỉ hiển thị tên cửa hàng (không có mã) chưa?
- [ ] Độ rộng đã tính đến 全角16文字 chưa? Dữ liệu mẫu đã dùng chuỗi tối đa chưa?
- [ ] Chức năng 前週/今週/翌週 đã phản ánh đúng spec (前週 disabled khi ở 今週; 翌週 xem được > 1 năm) chưa?
- [ ] Lỗi「アリア」đã sửa thành「エリア」chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-173] C000178_配送工事区分選択
**Feedback khách:**
- Thiết kế button 時間帯 → align theo màn 配送情報変更_時間帯選択
- Tạo thêm design khi keyboard hiển thị (lúc nhập 工事重み)
- Khi 時間帯 = 0件: hiển thị「0/10」, button非活性
- Guide message phải phù hợp với nội dung màn này (không dùng guide của 予約担当者入力)
- Vùng「エリア」hiển thị tên khu vực giao hàng/công trình (水戸, いわき...) không phải 店舗コード/店舗名

- [ ] Button 時間帯 đã khớp thiết kế màn 配送情報変更_時間帯選択 chưa?
- [ ] Design khi keyboard hiển thị đã được tạo chưa?
- [ ] Design khi 時間帯 = 0件 (hiển thị「0/10」, button非活性) đã được tạo chưa?
- [ ] Guide message đã được cập nhật phù hợp với màn hình này chưa?
- [ ] Vùng「エリア」đã hiển thị tên khu vực (水戸, いわき...) thay vì 店舗コード chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-174] C000180_指定方法選択
**Feedback khách:**
- Từ「指定方法」xuất hiện 2 lần — xóa guide「～を選択してください」và vùng xanh「検索方法」
- Button「閉じる」quá to so với button chính (trông như 3 lựa chọn) — thu nhỏ khớp màn khác

- [ ] Guide「～を選択してください」và vùng xanh「検索方法」đã được xóa chưa?
- [ ] Kích thước button「閉じる」đã được thu nhỏ cho khớp với màn khác chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-175] B0401エリア絞込
**Feedback khách:**
- エリアコード → căn giữa (中央揃え)
- Độ rộng cột エリア名称 tính đến tối đa 全角30文字; điều chỉnh kích thước subform
- Dữ liệu mẫu: mỗi dòng khác nhau
- Scrollbar không đè lên明細
- Đổi tên button「進む」→「確定」
- Xóa button「特定エリア表示」(chức năng không còn dùng)

- [ ] エリアコード đã căn giữa chưa?
- [ ] Độ rộng cột エリア名称 đã đủ cho 全角30文字 chưa? Kích thước subform đã điều chỉnh chưa?
- [ ] Dữ liệu mẫu mỗi dòng có nội dung khác nhau chưa?
- [ ] Scrollbar không đè lên明細 chưa?
- [ ] Button「進む」đã đổi thành「確定」chưa?
- [ ] Button「特定エリア表示」đã được xóa chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-176] C000181_JISコード入力
**Feedback khách:**
- Tạo cả design chưa nhập (未入力) và đã nhập (入力済み) — địa chỉ hiển thị「都道府県＋市」
- JISコード, 配送頻度 → căn giữa
- Sửa lỗi chữ Hán trong「頻度」
- Dữ liệu mẫu mỗi dòng khác nhau; scrollbar không đè lên明細
- Xóa button「確定」(không cần); button「印刷」→ đổi thành màu xanh
- Tạo thêm design màn hình sau khi nhấn「宅配不可エリア」

- [ ] Design trạng thái chưa nhập (未入力) đã có chưa?
- [ ] Design trạng thái đã nhập (入力済み) với địa chỉ「都道府県＋市」đã có chưa?
- [ ] JISコード, 配送頻度 đã căn giữa chưa?
- [ ] Lỗi chữ Hán「頻」đã sửa đúng chưa?
- [ ] Dữ liệu mẫu mỗi dòng khác nhau chưa?
- [ ] Scrollbar không đè lên明細 chưa?
- [ ] Button「確定」đã được xóa chưa?
- [ ] Button「印刷」đã đổi sang màu xanh chưa?
- [ ] Design màn sau khi nhấn「宅配不可エリア」đã được tạo chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-178] C000182_店舗情報入力
**Feedback khách:**
- Tạo cả design chưa nhập và đã nhập — địa chỉ hiển thị「都道府県＋市」
- JISコード, 配送頻度 → căn giữa; sửa lỗi chữ Hán「頻」
- Dữ liệu mẫu mỗi dòng khác nhau; scrollbar không đè lên明細
- Màn này là「配送工事エリア担当店舗照会」hiện hành → xóa button「確定」; button「印刷」→ màu xanh
- Tạo thêm design màn hình sau khi nhấn「宅配不可エリア」

- [ ] Design trạng thái chưa nhập (未入力) đã có chưa?
- [ ] Design trạng thái đã nhập (入力済み) với địa chỉ「都道府県＋市」đã có chưa?
- [ ] JISコード, 配送頻度 đã căn giữa chưa?
- [ ] Lỗi chữ Hán「頻」đã sửa đúng chưa?
- [ ] Dữ liệu mẫu mỗi dòng khác nhau chưa?
- [ ] Scrollbar không đè lên明細 chưa?
- [ ] Button「確定」đã được xóa chưa?
- [ ] Button「印刷」đã đổi sang màu xanh chưa?
- [ ] Design màn sau khi nhấn「宅配不可エリア」đã được tạo chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-201] C000047_客先配送予定日
**Feedback khách:** Align thiết kế theo màn 配送情報変更_時間帯選択.

- [ ] Thiết kế đã khớp với màn 配送情報変更_時間帯選択 chưa?
- [ ] Upload bản sửa + đổi status → 20_確認待ち

---

### [POS_UI-203] C000183_空き状況一覧表示
**Feedback khách:** Ticket này có thể trùng với POS_UI-171 (thiếu hiển thị センター店名). Cần xác nhận có phải ticket thừa không.

- [ ] Xác nhận với PM: ticket này có trùng với POS_UI-171 không?
- [ ] Nếu trùng → đóng ticket này
- [ ] Nếu không trùng → xử lý theo yêu cầu cụ thể

---

*Tổng: 45 tickets | Ngày tổng hợp: 2026-05-24*
