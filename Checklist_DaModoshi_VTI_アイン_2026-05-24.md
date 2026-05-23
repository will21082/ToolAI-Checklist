# SHARP POS UI — Design Review Checklist
### Tổng hợp từ feedback 差戻 của VTI アイン · Áp dụng chuẩn Checklist_Screen_Design_VN.md

| Mục | Giá trị |
|---|---|
| Project | POS_UI — siconnect.backlog.com |
| Assignee | VTI アイン |
| Tổng | 45 tickets · 127 check items |
| Ngày | 2026-05-24 |

**Cách dùng:** Sau khi sửa xong mỗi ticket, điền `OK` / `NOK` / `N/A` vào cột Round 1. Designer chỉ submit lên Backlog khi toàn bộ item = OK hoặc N/A.

---

## ⚠️ Ưu tiên cao — Due 2026-03-31

### ⚠️ [POS_UI-69] C000048_時間帯選択 · ⚠️ **Due: 2026-03-31**

> **Feedback khách:** アイン 
配送情報変更_時間帯選択にデザインを合わせてください。
*(ảnh đính kèm)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Thiết kế button 時間帯 có được đồng bộ theo chuẩn màn 配送情報変更_時間帯選択 không? | M | | | |  |

### ⚠️ [POS_UI-72] C000052_別紙案内 · ⚠️ **Due: 2026-03-31**

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Tab & Consistency | *(Chưa có comment — cần mở Backlog xem comment gốc trước khi check)* |  | | | | Due 2026-03-31 |

### ⚠️ [POS_UI-73] C000053_お客様情報 · ⚠️ **Due: 2026-03-31**

> **Feedback khách:** 以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Tab & Consistency | Các sửa đổi theo comment gốc tại POS_UI-40 có được áp dụng đầy đủ không? |  | | | | Due 2026-03-31 — cần mở POS_UI-40 xem comment |

### ⚠️ [POS_UI-82] A0426_新黒伝決済（お預かり金額入力） · ⚠️ **Due: 2026-03-31**

> **Feedback khách:** 他のメニューとデザインが異なりますので統一をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Tab & Consistency | Thiết kế (màu, font, button, layout) có được đồng bộ với các menu khác trong cùng hệ thống không? | M | | | | Due 2026-03-31 |

---

## Nhóm 決済系

### [POS_UI-194] 返品エラー通知

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Tab & Consistency | *(Chưa có comment — xem Backlog)* |  | | | |  |

### [POS_UI-195] 元伝と新黒決済確認

> **Feedback khách:** アイン 
*(ảnh đính kèm)*
・お買上げ総数、総額については、最新のデザインに反映をお願いします。（画像赤枠）
・未決済金額について、デザインに反映をお願いします。（画像青枠）
*(ảnh đính kèm)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ | お買上げ総数・総額 có được cập nhật theo design mới nhất không? (xem ảnh vùng đỏ) | M | | | |  |
| 2 | Hiển thị & Đồng bộ | 未決済金額 có được thêm vào design không? (xem ảnh vùng xanh) | M | | | |  |

### [POS_UI-196] C000058_決済種別変更の確認

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Tab & Consistency | *(Chưa có comment — xem Backlog)* |  | | | |  |

### [POS_UI-197] 元伝カード決済引き継ぎの確認

> **Feedback khách:** アイン 
上に表示している「元伝カード決済」のタイトルは削除でお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề「元伝カード決済」ở phía trên màn hình có được xóa không? | M | | | |  |

### [POS_UI-198] 元伝決済時カード持ち確認

> **Feedback khách:** アイン 
・上に表示している「元伝決済時カード」のタイトルは削除でお願いします。
・「元伝決済時カード」を選択後は、自動で画面遷移する想定でしょうか。
　確定ボタンのようなものがないため確認です。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề「元伝決済時カード」ở phía trên màn hình có được xóa không? | M | | | |  |
| 2 | Screen Flow & Luồng XL | Spec chuyển màn sau khi chọn「元伝決済時カード」(tự động hay cần button?) có được xác nhận với khách trước khi thiết kế không? |  | | | | Cần hỏi khách — hiện không có button xác nhận |

---

## Nhóm 請求書・印刷系

### [POS_UI-140] C000101_請求書一覧／納品書一覧表示

> **Feedback khách:** アイン 
・Figmaの画面遷移図には請求書印刷の明細画面もありますので、こちらに添付をお願いします。
・請求書、納品書印刷画面では商品明細の追加、削除、修正は行えません。
　商品明細が編集できない前提のデザインにしていただけますでしょうか。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Screen Flow & Luồng XL | Màn hình明細 in 請求書 có được thêm vào Figma 画面遷移図 không? |  | | | |  |
| 2 | Screen Flow & Luồng XL | Màn hình in 請求書/納品書 có được thiết kế theo hướng 商品明細 read-only (không có nút thêm/xóa/sửa) không? | M | | | |  |

### [POS_UI-148] C000103_請求書日付

> **Feedback khách:** アイン 
以下修正をお願いします。
・販売担当者ではなく、印刷担当者に修正
・「元伝の決済」ラベルは不要
・請求書発行時は日付が必ず決まっているので、「予定日未定」チェックボックスは削除
・【請求書　印刷サンプル】の枠線で囲まれた～ の文は１行に収める
・【法求出 印刷サンプル】→【請求書　印刷サンプル】に修正
・文言の位置は以下画像に合わせる
*(ảnh đính kèm)*
・フッターの進捗バーは不要
※既成のデザインを流用いただくのは問題ありませんが、現行画面を見比べていただきますようお願いいたします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ | Label có được đổi「販売担当者」→「印刷担当者」không? | M | | | |  |
| 2 | Hiển thị & Đồng bộ | Label「元伝の決済」không cần thiết có được xóa không? |  | | | |  |
| 3 | UI Components & Controls | Checkbox「予定日未定」có được xóa không? (ngày luôn xác định khi phát hành hóa đơn) | M | | | |  |
| 4 | Cấu trúc Layout & Vị trí | Văn bản trong khung【請求書　印刷サンプル】có được gói gọn trong 1 dòng không? |  | | | |  |
| 5 | Hiển thị & Đồng bộ | Tên khung【法求出 印刷サンプル】có được sửa thành【請求書　印刷サンプル】không? |  | | | |  |
| 6 | Header & Navigation | Footer progress bar không cần thiết có được xóa không? |  | | | |  |

### [POS_UI-149] C000104_お支払予定日

> **Feedback khách:** アイン 
以下修正をお願いします。
・販売担当者ではなく、印刷担当者に修正
・「お支払予定日」ラベル1つのみ表示
・請求書発行時は日付が必ず決まっているので、「予定日未定」チェックボックスは削除
・【請求書　印刷サンプル】の枠線で囲まれた～ の文は１行に収める
・【法求出 印刷サンプル】→【請求書　印刷サンプル】に修正
・赤枠の位置が違います。添付画像青枠の位置にする
*(ảnh đính kèm)*
・文言の位置は以下画像に合わせる
*(ảnh đính kèm)*
・フッターの進捗バーは不要
※既成のデザインを流用いただくのは問題ありませんが、現行画面を見比べていただきますようお願いいたします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ | Label có được đổi「販売担当者」→「印刷担当者」không? | M | | | |  |
| 2 | Hiển thị & Đồng bộ | Label「お支払予定日」có chỉ hiển thị 1 lần không? |  | | | |  |
| 3 | UI Components & Controls | Checkbox「予定日未定」có được xóa không? | M | | | |  |
| 4 | Cấu trúc Layout & Vị trí | Văn bản trong khung【請求書　印刷サンプル】có được gói gọn trong 1 dòng không? |  | | | |  |
| 5 | Hiển thị & Đồng bộ | Tên khung【法求出 印刷サンプル】có được sửa thành【請求書　印刷サンプル】không? |  | | | |  |
| 6 | Header & Navigation | Footer progress bar không cần thiết có được xóa không? |  | | | |  |

### [POS_UI-150] C000105_お客様氏名

> **Feedback khách:** アイン 
販売担当者ではなく、印刷担当者に修正をお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ | Label có được đổi「販売担当者」→「印刷担当者」không? | M | | | |  |

### [POS_UI-151] C000106_摘要入力

> **Feedback khách:** アイン 
摘要入力は1行全角４５文字×５行となります。
”MAX文字数入れたデザインの作成をお願いします。
もし余白が余る場合は、調整をお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Input Fields & Form | Textbox có thể hiện đúng spec 1行全角45文字×5行 không? | M | | | |  |
| 2 | Input Fields & Form | Thiết kế có bao gồm trường hợp MAX văn bản (45×5) không? | M | | | |  |
| 3 | Cấu trúc Layout & Vị trí | Nếu thừa khoảng trắng sau MAX text, layout có được điều chỉnh lại không? |  | | | |  |

### [POS_UI-184] C000126_印刷確認

> **Feedback khách:** アイン 
・「お客様控えのみ」「会員番号記載」のみでは直感的に分かりにくいため、
「お客様控えのみを印刷」「見積書に会員番号を記載」に文言変更をお願いします。

・「C000124_未印刷一覧表示」で印刷をする場合、現行では以下のデザイン、流れになります。
*(ảnh đính kèm)*
↓
*(ảnh đính kèm)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | UI Components & Controls | Text button có được đổi thành「お客様控えのみを印刷」không? | M | | | | Từ cũ ngắn, không trực quan |
| 3 | UI Components & Controls | Text button có được đổi thành「見積書に会員番号を記載」không? | M | | | |  |
| 4 | Screen Flow & Luồng XL | Flow in từ màn「未印刷一覧表示」có phản ánh đúng flow hiện hành (xem ảnh đính kèm) không? |  | | | |  |

---

## Nhóm 見積書未印刷系
> ⚡ Lưu ý chung: **Tất cả màn trong nhóm này phải đổi tiêu đề → 「見積書未印刷一覧（配送端末）」**

### [POS_UI-155] C000110_検索方法選択

> **Feedback khách:** アイン 
五月雨式で申し訳ありませんが、以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Các sửa đổi theo comment POS_UI-180 (C000123) có được áp dụng đồng bộ cho màn này không? |  | | | | C000110 và C000123 cùng loại màn |

### [POS_UI-157] C000111_未承認一覧表示

> **Feedback khách:** アイン 
申し訳ございません。
以下コメントの
「・以下画像赤枠の機能ボタン（端末見積検索は除く）は引き継ぎたいので、ボタンを追加 または 別の手段で機能が実行できるようなデザインに修正」
については、ボタン配置場所の検討を進めますので一旦保留でお願いいたします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Yêu cầu thêm button chức năng (vùng đỏ) đang **保留** — có xác nhận chưa làm trong round này không? |  | | | | Không cần làm — chờ khách confirm vị trí button |

### [POS_UI-158] C000114_詳細

> **Feedback khách:** アイン 
現行ではあんしんパスポート会員ではない顧客の見積書の場合は、その旨を表示しています。
この仕様は引き継ぎたいため、デザインの追加をお願いします。
*(ảnh đính kèm)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ | Khi khách hàng không phải hội viên あんしんパスポート, màn hình có hiển thị thông báo tương ứng (giống hiện hành) không? | M | | | | Xem ảnh đính kèm trong ticket |

### [POS_UI-160] C000115_別紙内容確認

> **Feedback khách:** アイン 
*(link)*
申し訳ございません。上記コメントについてです。
添付画像の画面「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加するデザインにしていただきますようお願いします。
*(ảnh đính kèm)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Màn hình C000114_詳細 có được thêm tab「別紙内容確認」không? | M | | | | Xem ảnh đính kèm |

### [POS_UI-161] C000116_次回訪問予定

> **Feedback khách:** アイン 
以下コメントの対応をお願いします。
*(link)*
「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Màn hình C000114_詳細 có được thêm tab「次回訪問予定」không? | M | | | |  |

### [POS_UI-162] C000117_見積内容

> **Feedback khách:** アイン 
以下コメントの対応をお願いします。
*(link)*
「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Màn hình C000114_詳細 có được thêm tab「見積内容」không? | M | | | |  |

### [POS_UI-163] C000118_見積結果

> **Feedback khách:** アイン 
以下コメントの対応をお願いします。
*(link)*
「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Màn hình C000114_詳細 có được thêm tab「見積結果」không? | M | | | |  |

### [POS_UI-165] C000120_店舗への連絡

> **Feedback khách:** アイン 
以下コメントの対応をお願いします。
*(link)*
「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Màn hình C000114_詳細 có được thêm tab「店舗への連絡」không? | M | | | |  |

### [POS_UI-166] C000121_コメント

> **Feedback khách:** アイン 
以下コメントの対応をお願いします。
*(link)*
「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Màn hình C000114_詳細 có được thêm tab「コメント」không? | M | | | |  |

### [POS_UI-180] C000123_検索方法選択

> **Feedback khách:** アイン 
以下検討をお願いします。
・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
・担当者画面に表示ではなく、白背景に選択画面を表示するデザインにできますでしょうか。
簡単なイメージになります。
*(ảnh đính kèm)*
・"検索方法"という単語が３回出てくるため、過剰に思います。
　ですので、タイトル：検索方法選択、「～を選択してください」のガイドを削除。
　緑背景＋囲み線は残して置き、緑背景の部分は”検索方法選択”という文言に修正をお願いします。
　また、「指定なし」を「指定せずに検索 」としてください。
・閉じるボタンと検索方法のボタンの幅が同じため、ぱっと見で３択に見えます。
　閉じるボタンのサイズは他画面に合わせてください。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | UI Components & Controls | Popup có dùng nền trắng (白背景), không đè lên màn 担当者 không? |  | | | |  |
| 3 | Header & Navigation | Từ「検索方法」có chỉ xuất hiện 1 lần không? (guide và vùng xanh trùng đã xóa) |  | | | |  |
| 4 | UI Components & Controls | Vùng xanh lá đã được sửa thành text「検索方法選択」không? |  | | | |  |
| 5 | UI Components & Controls | Nút「指定なし」có được đổi thành「指定せずに検索」không? |  | | | |  |
| 6 | UI Components & Controls | Kích thước button「閉じる」có được thu nhỏ khớp màn khác không? |  | | | | Hiện trông như 3 lựa chọn |

### [POS_UI-181] C000125_端末見積書検索サブフォーム

> **Feedback khách:** アイン 
・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
・以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Các sửa đổi theo comment POS_UI-156 có được áp dụng không? |  | | | | Cần mở POS_UI-156 xem comment |

### [POS_UI-182] C000124_未承認一覧表示

> **Feedback khách:** アイン 
以下修正をお願いします。
・本チケットのタイトルを「C000124_未印刷一覧表示」に修正をお願いします。
・タイトルは「見積書未印刷一覧（配送端末）」に修正
・選択列のヘッダーはチェックボックスコントロールを置かずに、文言"選択"にする
・以下画像赤枠の機能ボタンは引き継ぎたいので、ボタンを追加 または 別の手段で機能が実行できるようなデザインに修正
*(ảnh đính kèm)*
　また、本機能は承認された見積書を印刷するメニューなので、青色ボタンは「印刷」にする
・スクロールバーが金額欄と重なっているため、重ならないように調整
　→ 売上画面のスクロールバー仕様と異なっている
・サンプルとして表示する明細情報は、Noごとに異なる内容にする
　あわせて、ツールチップ表示のデザインを追加
　→ 他画面についても同様に対応
・現行では1ページ18明細表示なので、可能な限り18明

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | UI Components & Controls | Header cột '選択' có dùng text「選択」thay vì checkbox control không? |  | | | |  |
| 3 | UI Components & Controls | Các button chức năng (vùng đỏ trong ảnh) có được thêm lại hoặc có giải pháp thay thế không? |  | | | |  |
| 4 | UI Components & Controls | Button xanh có được đặt tên「印刷」không? |  | | | | Đây là menu in見積書đã duyệt |
| 5 | Cấu trúc Layout & Vị trí | Scrollbar có không đè lên vùng金額欄 không? |  | | | |  |
| 6 | Hiển thị & Đồng bộ | Dữ liệu mẫu mỗi dòng có nội dung khác nhau không? |  | | | |  |
| 7 | UI Components & Controls | Vị trí hiển thị「...」có được thêm tooltip không? |  | | | |  |

### [POS_UI-183] C000127_詳細

> **Feedback khách:** アイン 
現行ではあんしんパスポート会員ではない顧客の見積書の場合は、その旨を表示しています。
この仕様は引き継ぎたいため、デザインの追加をお願いします。
*(ảnh đính kèm)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Hiển thị & Đồng bộ | Khi khách hàng không phải hội viên あんしんパスポート, màn hình có hiển thị thông báo tương ứng không? | M | | | | Xem ảnh đính kèm |

### [POS_UI-185] C000128_別紙内容確認

> **Feedback khách:** アイン 
・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
・以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Các sửa đổi theo comment đã có trong ticket có được áp dụng không? |  | | | |  |

### [POS_UI-186] C000129_次回訪問予定

> **Feedback khách:** アイン 
・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
・以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Các sửa đổi theo comment đã có trong ticket có được áp dụng không? |  | | | |  |

### [POS_UI-187] C000130_見積内容

> **Feedback khách:** アイン 
・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
・以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Các sửa đổi theo comment đã có trong ticket có được áp dụng không? |  | | | |  |

### [POS_UI-188] C000131_見積結果

> **Feedback khách:** アイン 
・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
・以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Các sửa đổi theo comment đã có trong ticket có được áp dụng không? |  | | | |  |

### [POS_UI-190] C000133_店舗への連絡

> **Feedback khách:** アイン 
・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
・以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Các sửa đổi theo comment đã có trong ticket có được áp dụng không? |  | | | |  |

### [POS_UI-191] C000134_コメント

> **Feedback khách:** アイン 
・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
・以下コメントの対応をお願いします。
*(link)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề có được đổi thành「見積書未印刷一覧（配送端末）」không? | M | | | |  |
| 2 | Tab & Consistency | Các sửa đổi theo comment POS_UI-166 có được áp dụng không? |  | | | |  |

---

## Nhóm 配送・予約系

### [POS_UI-167] C000185_明細入力

> **Feedback khách:** アイン 
以下修正をお願いします。
*(ảnh đính kèm)*
・型番の文字数が少ないと思います。
　表形式ではなく、売上と同じカード形式としていただきますようお願いします。
・このメニューは1取引3明細までとなりますので3明細分は表示できるよう調整をお願いします。
・”...”を表示する箇所はツールチップを表示する認識です。ツールチップの表示を含めたデザインの作成をお願いします。
・型番での検索も可能ですので、型番検索ボタン または 他の手段をデザインに反映をお願いします。
・「取消」を「在庫予約を取消」に修正をお願いします。
　また、「取消」は戻る系のボタンになりますので、左側に配置をお願いします。
・予約を試みたが、在庫がない場合はNo１のような表示になりますので、こちらのデザイン作成をお願いします。
　作成後は、本チケットに添付をお願いします。
*(ảnh đính kèm)

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Cấu trúc Layout & Vị trí | Hiển thị明細 có được đổi từ bảng (表形式) sang dạng card (カード形式) giống màn 売上 không? | M | | | | Lý do: 型番 quá ngắn khi dùng bảng |
| 2 | Cấu trúc Layout & Vị trí | Tối đa 3明細/giao dịch có đủ không gian hiển thị không? | M | | | |  |
| 3 | UI Components & Controls | Các vị trí hiển thị「...」có được thêm tooltip không? |  | | | |  |
| 4 | Input Fields & Form | Chức năng tìm kiếm theo 型番 có button hoặc giải pháp khác được thiết kế không? |  | | | |  |
| 5 | UI Components & Controls | Button「取消」có được đổi tên thành「在庫予約を取消」không? | M | | | |  |
| 6 | Cấu trúc Layout & Vị trí | Button「在庫予約を取消」(戻る系) có được đặt ở bên trái không? |  | | | |  |
| 7 | Hiển thị & Đồng bộ | Thiết kế trường hợp không có tồn kho (在庫なし, No1) có được tạo không? |  | | | |  |

### [POS_UI-169] C000186_在庫引当確認 / 予約取消確認

> **Feedback khách:** アイン 
以下修正をお願いします。
・本来伝えなければならない”DC在庫引当を行いますか。”のフォントサイズが小さく目立たない印象ですので、フォントサイズを上げて下さい。
　また、タイトルと本文で同じ内容かと思いますのでタイトルを削除し、本文は「DC在庫の引当を行いますか。」としてください
・選択肢は「いいえ」「はい」としてください。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Font size của câu「DC在庫の引当を行いますか。」có đủ lớn và nổi bật không? |  | | | |  |
| 2 | Header & Navigation | Tiêu đề trùng nội dung với body có được xóa không? |  | | | |  |
| 3 | Hiển thị & Đồng bộ | Body text có được sửa thành「DC在庫の引当を行いますか。」không? | M | | | |  |
| 4 | UI Components & Controls | Lựa chọn có được đổi thành「いいえ」「はい」không? | M | | | |  |

### [POS_UI-171] C000176_空き状況一覧表示

> **Feedback khách:** アイン 
以下ご対応のほどよろしくお願いいたします。
・「センター店」表示エリアの"９１１２:試験配送センター"ですが、左側の表示エリアに"011-9112"（法人-店舗コード）が表示されているため、
　店舗名のみの表示でお願いします。
　また、店舗名は最大全角16文字ですので、そちらを考慮した表示幅にしてください。
　表示するデータも最大文字数としてください。

・前週 今週 翌週 の切替ですが、現在は以下の仕様となっております
　→現在表示している情報が今週の場合は「前週」の切替不可
　→1年以上先の情報も確認できるよう、「翌週」は1週間先のみではない（例：当営業日は2026/5/14の場合、2027/6/14 先も確認可能）
　ですので、これを踏まえたデザインの作成をお願いします。

・"エリア" が "アリア" になっているので、"エリア"に修正をお願いします。

・枠数は最大3桁

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ | Vùng「センター店」có chỉ hiển thị 店舗名 (không hiển thị 法人-店舗コード vì đã có ở vùng trái) không? | M | | | |  |
| 2 | Cấu trúc Layout & Vị trí | Độ rộng cột 店舗名 có tính đến tối đa 全角16文字 không? Dữ liệu mẫu có dùng chuỗi tối đa không? |  | | | |  |
| 3 | Screen Flow & Luồng XL | Chức năng 前週/今週/翌週 có phản ánh đúng spec: 今週 → 前週 disabled; 翌週 xem được > 1 năm không? |  | | | |  |
| 4 | Hiển thị & Đồng bộ | Lỗi chính tả「アリア」có được sửa thành「エリア」không? | M | | | |  |

### [POS_UI-173] C000178_配送工事区分選択

> **Feedback khách:** アイン 
・時間帯の各ボタンデザインについては、配送情報変更_時間帯選択にデザインを合わせてください。
*(ảnh đính kèm)*

・工事重み（数値）を入力する際キーボードが表示されると思いますので、キーボードを表示させたデザインの作成もお願いします。

・時間帯の件数が０件の場合は0/10の表記で、ボタンの状態は非活性となり押せない挙動になります。
　こちらのデザインについても作成をお願いします。
　また、他メニューでも同じ画面がありましたら合わせて対応をお願いします。

・ガイドメッセージが予約担当者入力時の内容ですので、画面に合わせた内容に修正をお願いします。

・エリアは店舗コード、店舗名ではなく、配送や工事エリア（水戸やいわき など）になりますので、デザインに反映をお願いします。

・本機能は「配送工事費予約」と統合されており、当該機能には予約画面でエリアの説明コメントを

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Thiết kế button 時間帯 có được đồng bộ theo chuẩn màn 配送情報変更_時間帯選択 không? | M | | | |  |
| 2 | Input Fields & Form | Thiết kế màn hình khi keyboard hiển thị (lúc nhập 工事重み) có được tạo không? |  | | | |  |
| 3 | UI Components & Controls | Khi 時間帯 = 0件, có hiển thị「0/10」và button ở trạng thái 非活性 không? |  | | | |  |
| 4 | Header & Navigation | Guide message có được cập nhật phù hợp với màn này (không dùng guide của 予約担当者入力) không? |  | | | |  |
| 5 | Hiển thị & Đồng bộ | Vùng「エリア」có hiển thị tên khu vực giao hàng/công trình (水戸, いわき...) thay vì 店舗コード không? | M | | | |  |

### [POS_UI-174] C000180_指定方法選択

> **Feedback khách:** アイン 
"指定方法"という単語が２回出てくるため、過剰に思います。※一部検索方法になっている
ですので、タイトル：指定方法を選択は残して置き、「～を選択してください」のガイドは削除してください。
緑背景の検索方法も削除でお願いします。
また、閉じるボタンと検索方法のボタンの幅が同じため、ぱっと見で３択に見えます。
閉じるボタンのサイズは他画面に合わせてください。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Guide「～を選択してください」và vùng xanh lá「検索方法」có được xóa không? (từ「指定方法」đã có trong tiêu đề) |  | | | |  |
| 2 | UI Components & Controls | Kích thước button「閉じる」có được thu nhỏ khớp với các màn hình khác không? |  | | | | Hiện tại cùng cỡ button chính → trông như 3 lựa chọn |

### [POS_UI-175] B0401エリア絞込

> **Feedback khách:** アイン 
・エリアコードは中央揃えで表示してください。
・エリア名称は最大で全角３０文字なので、その文字数がゆとりある形で入る程度の列幅で問題ありません。
　そのうえで、サブフォームのサイズ調整をお願いします。
・同じデータが表示されることは想定していないため、表示データは各Noバラバラにしてください。
・スクロールバーが明細に被らないよう調整してください。
・ボタン名は「進む」ではなく、「確定」にしてください。

また、申し訳ありませんが「特定エリア表示」ボタンは削除でお願いします。
本メニューでは、現在使用されていない機能のようです。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Cấu trúc Layout & Vị trí | エリアコード có được căn giữa (中央揃え) không? | M | | | | Chuẩn: code → center |
| 2 | Cấu trúc Layout & Vị trí | Độ rộng cột エリア名称 có đủ cho tối đa 全角30文字 với margin thoải mái không? |  | | | |  |
| 3 | Cấu trúc Layout & Vị trí | Kích thước subform có được điều chỉnh sau khi sửa độ rộng cột không? |  | | | |  |
| 4 | Hiển thị & Đồng bộ | Dữ liệu mẫu mỗi dòng có nội dung khác nhau không? |  | | | |  |
| 5 | Cấu trúc Layout & Vị trí | Scrollbar có không đè lên vùng明細 không? |  | | | |  |
| 6 | UI Components & Controls | Button「進む」có được đổi thành「確定」không? | M | | | |  |
| 7 | UI Components & Controls | Button「特定エリア表示」có được xóa không? (chức năng không còn dùng) |  | | | |  |

### [POS_UI-176] C000181_JISコード入力

> **Feedback khách:** ・JISコード入力のテキストボックスには検索後、何が表示されますでしょうか？
　→JISコードのみでしょうか？それとも、都道府県＋市まで表示されますでしょうか？
　→未入力状態だけでなく、入力済みの状態のデザインの作成をお願いします。

・JISコード、配送頻度は中央揃えにしてください。

・"頻度"の"頻"の漢字が間違っています。

・住所は"ミトミツクニ"ではなく、都道府県＋市の表示にしてください。

・データは各明細で別の内容にしてください。

・スクロールバーは明細に被らないよう調整をお願いします。

・この画面は現行の「配送工事エリア担当店舗照会」のデザインだと思われますが、認識合っておりますか？
　合っている場合、「確定ボタン」は不要でお願いします。
　また、「印刷ボタン」を青いボタンにしてください。

・「宅配不可エリア」ボタンを押した後の画面デザイン作成をお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Input Fields & Form | Thiết kế trạng thái chưa nhập (未入力) có tồn tại không? | M | | | |  |
| 2 | Input Fields & Form | Thiết kế trạng thái đã nhập (入力済み) với địa chỉ「都道府県＋市」có tồn tại không? | M | | | |  |
| 3 | Cấu trúc Layout & Vị trí | JISコード và 配送頻度 có được căn giữa không? | M | | | |  |
| 4 | Hiển thị & Đồng bộ | Lỗi chữ Hán trong「頻度」có được sửa đúng không? | M | | | |  |
| 5 | Hiển thị & Đồng bộ | Địa chỉ có hiển thị「都道府県＋市」thay vì「ミトミツクニ」không? | M | | | |  |
| 6 | Hiển thị & Đồng bộ | Dữ liệu mẫu mỗi dòng có nội dung khác nhau không? |  | | | |  |
| 7 | Cấu trúc Layout & Vị trí | Scrollbar có không đè lên vùng明細 không? |  | | | |  |
| 8 | UI Components & Controls | Button「確定」có được xóa không? |  | | | |  |
| 9 | UI Components & Controls | Button「印刷」có được đổi sang màu xanh không? |  | | | |  |
| 10 | Screen Flow & Luồng XL | Màn hình sau khi nhấn「宅配不可エリア」có được thiết kế không? |  | | | |  |

### [POS_UI-178] C000182_店舗情報入力

> **Feedback khách:** アイン 
・法人検索、店舗検索のテキストボックスには検索後、何が表示されますでしょうか？
　→法人、店舗コードのみでしょうか？それとも、法人コードと法人名、店舗コードと店舗名でしょうか？
　→未入力状態だけでなく、入力済みの状態のデザインの作成をお願いします。

・JISコード、配送頻度は中央揃えにしてください。

・"頻度"の"頻"の漢字が間違っています。

・住所は"ミトミツクニ"ではなく、都道府県＋市の表示にしてください。

・データは各明細で別の内容にしてください。

・スクロールバーは明細に被らないよう調整をお願いします。

・この画面は現行の「配送工事エリア担当店舗照会」のデザインだと思われますが、認識合っておりますか？
　合っている場合、「確定ボタン」は不要でお願いします。
　また、「印刷ボタン」を青いボタンにしてください。

・「宅配不可エリア」ボタンを押した後の画面デザイ

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Input Fields & Form | Thiết kế trạng thái chưa nhập (未入力) có tồn tại không? | M | | | |  |
| 2 | Input Fields & Form | Thiết kế trạng thái đã nhập (入力済み) với địa chỉ「都道府県＋市」có tồn tại không? | M | | | |  |
| 3 | Cấu trúc Layout & Vị trí | JISコード và 配送頻度 có được căn giữa không? | M | | | |  |
| 4 | Hiển thị & Đồng bộ | Lỗi chữ Hán trong「頻度」có được sửa đúng không? | M | | | |  |
| 5 | Hiển thị & Đồng bộ | Địa chỉ có hiển thị「都道府県＋市」thay vì「ミトミツクニ」không? | M | | | |  |
| 6 | Hiển thị & Đồng bộ | Dữ liệu mẫu mỗi dòng có nội dung khác nhau không? |  | | | |  |
| 7 | Cấu trúc Layout & Vị trí | Scrollbar có không đè lên vùng明細 không? |  | | | |  |
| 8 | UI Components & Controls | Button「確定」có được xóa không? |  | | | |  |
| 9 | UI Components & Controls | Button「印刷」có được đổi sang màu xanh không? |  | | | |  |
| 10 | Screen Flow & Luồng XL | Màn hình sau khi nhấn「宅配不可エリア」có được thiết kế không? |  | | | |  |

### [POS_UI-201] C000047_客先配送予定日

> **Feedback khách:** アイン 
配送情報変更_時間帯選択にデザインを合わせてください。
*(ảnh đính kèm)*

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Thiết kế button 時間帯 có được đồng bộ theo chuẩn màn 配送情報変更_時間帯選択 không? | M | | | |  |

### [POS_UI-203] C000183_空き状況一覧表示

> **Feedback khách:** アイン 
*(link)* と重複しているようです。（センター店名の表示がありません）
不要なチケットである可能性がありますので、ご確認をお願いします。

| # | Nhóm | Check Item | M | Round 1 | Round 2 | Round 3 | Remark |
|---|---|---|---|---|---|---|---|
| 1 | Screen Flow & Luồng XL | Ticket này có được xác nhận là trùng với POS_UI-171 không? Nếu trùng → đóng ticket. |  | | | | Khách đã comment: 重複している可能性あり |

---

*Tổng: 45 tickets — 127 check items · Ngày: 2026-05-24*