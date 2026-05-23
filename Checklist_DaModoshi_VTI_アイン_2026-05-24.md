# SHARP POS UI — Design Review Checklist
> Tổng hợp từ Backlog · Assignee: VTI アイン · Status: 30_差戻／修正依頼

| | |
|---|---|
| Tổng tickets | 45 |
| Tổng check items | 133 |
| Ngày tổng hợp | 2026-05-24 |
| Chuẩn áp dụng | Checklist_Screen_Design_VN.md |

**Cách dùng:** Sau khi sửa xong mỗi ticket → điền `OK` / `NOK` / `N/A` vào Round 1 → upload Backlog → đổi status `20_確認待ち`.

---

## [POS_UI-69] C000048_時間帯選択 · ⚠️ Due: **2026-03-31**
- Màn hình: C000048
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-69

**Feedback khách:**
> 。
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Thiết kế button 時間帯 đã được đồng bộ theo chuẩn màn 配送情報変更_時間帯選択 chưa? | POS_UI-69 | | | | M |  |

---

## [POS_UI-72] C000052_別紙案内 · ⚠️ Due: **2026-03-31**
- Màn hình: C000052
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-18
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-72

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Tab & Thông tin Chi tiết / Consistency | *(Chưa có comment — cần mở Backlog xem comment gốc)* | POS_UI-72 | | | |  | Due 2026-03-31 |

---

## [POS_UI-73] C000053_お客様情報 · ⚠️ Due: **2026-03-31**
- Màn hình: C000053
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-07
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-73

**Feedback khách:**
> 以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment gốc tại POS_UI-40 đã được áp dụng đầy đủ chưa? | POS_UI-73 | | | |  | Cần mở POS_UI-40 xem comment. Due 2026-03-31 |

---

## [POS_UI-82] A0426_新黒伝決済（お預かり金額入力） · ⚠️ Due: **2026-03-31**
- Màn hình: A0426
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-07
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-82

**Feedback khách:**
> 他のメニューとデザインが異なりますので統一をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Tab & Thông tin Chi tiết / Consistency | Thiết kế (màu, font, button, layout) đã được đồng bộ với các menu khác trong cùng hệ thống chưa? | POS_UI-82 | | | | M | Due 2026-03-31 |

---

## [POS_UI-139] C000095_明細入力
- Màn hình: C000095
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-18
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-139

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Tab & Thông tin Chi tiết / Consistency | *(Chưa có comment — cần mở Backlog xem comment gốc)* | POS_UI-139 | | | |  |  |

---

## [POS_UI-140] C000101_請求書一覧／納品書一覧表示
- Màn hình: C000101
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-07
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-140

**Feedback khách:**
> 、こちらに添付をお願いします。
> ・請求書、納品書印刷画面では商品明細の追加、削除、修正は行えません。
> 商品明細が編集できない前提のデザインにしていただけますでしょうか。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Screen Flow & Luồng Xử lý | Màn hình 明細 in 請求書 đã được thêm vào Figma 画面遷移図 chưa? | POS_UI-140 | | | |  |  |
| 2 | Screen Flow & Luồng Xử lý | Màn hình in 請求書/納品書 đã được thiết kế theo hướng 商品明細 read-only (không có nút thêm/xóa/sửa) chưa? | POS_UI-140 | | | | M |  |

---

## [POS_UI-148] C000103_請求書日付
- Màn hình: C000103
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-148

**Feedback khách:**
> 。
> ・販売担当者ではなく、印刷担当者に修正
> ・「元伝の決済」ラベルは不要
> ・請求書発行時は日付が必ず決まっているので、「予定日未定」チェックボックスは削除
> ・【請求書　印刷サンプル】の枠線で囲まれた～ の文は１行に収める
> ・【法求出 印刷サンプル】→【請求書　印刷サンプル】に修正
> ・文言の位置は以下画像に合わせる
> *(ảnh đính kèm)*
> ・フッターの進捗バーは不要
> ※既成のデザインを流用いただくのは問題ありませんが、現行画面を見比べていただきますようお願いいたします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ Thông tin | Label đã đổi「販売担当者」→「印刷担当者」chưa? | POS_UI-148 | | | | M |  |
| 2 | Hiển thị & Đồng bộ Thông tin | Label「元伝の決済」không cần thiết đã được xóa chưa? | POS_UI-148 | | | |  |  |
| 3 | UI Components & Controls | Checkbox「予定日未定」đã được xóa chưa? (ngày luôn xác định khi phát hành hóa đơn) | POS_UI-148 | | | | M |  |
| 4 | Cấu trúc Layout & Vị trí Thông tin | Văn bản trong khung【請求書　印刷サンプル】đã được gói gọn trong 1 dòng chưa? | POS_UI-148 | | | |  |  |
| 5 | Hiển thị & Đồng bộ Thông tin | Tên khung【法求出 印刷サンプル】đã sửa thành【請求書　印刷サンプル】chưa? | POS_UI-148 | | | |  |  |
| 6 | Header & Navigation | Footer progress bar không cần thiết đã được xóa chưa? | POS_UI-148 | | | |  |  |

---

## [POS_UI-149] C000104_お支払予定日
- Màn hình: C000104
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-149

**Feedback khách:**
> 。
> ・販売担当者ではなく、印刷担当者に修正
> ・「お支払予定日」ラベル1つのみ表示
> ・請求書発行時は日付が必ず決まっているので、「予定日未定」チェックボックスは削除
> ・【請求書　印刷サンプル】の枠線で囲まれた～ の文は１行に収める
> ・【法求出 印刷サンプル】→【請求書　印刷サンプル】に修正
> ・赤枠の位置が違います。添付画像青枠の位置にする
> *(ảnh đính kèm)*
> ・文言の位置は以下画像に合わせる
> *(ảnh đính kèm)*
> ・フッターの進捗バーは不要
> ※既成のデザインを流用いただくのは問題ありませんが、現行画面を見比べていただきますようお願いいたします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ Thông tin | Label đã đổi「販売担当者」→「印刷担当者」chưa? | POS_UI-149 | | | | M |  |
| 2 | Hiển thị & Đồng bộ Thông tin | Label「お支払予定日」đã chỉ hiển thị 1 lần chưa? | POS_UI-149 | | | |  |  |
| 3 | UI Components & Controls | Checkbox「予定日未定」đã được xóa chưa? | POS_UI-149 | | | | M |  |
| 4 | Cấu trúc Layout & Vị trí Thông tin | Văn bản trong khung【請求書　印刷サンプル】đã được gói gọn trong 1 dòng chưa? | POS_UI-149 | | | |  |  |
| 5 | Hiển thị & Đồng bộ Thông tin | Tên khung【法求出 印刷サンプル】đã sửa thành【請求書　印刷サンプル】chưa? | POS_UI-149 | | | |  |  |
| 6 | Header & Navigation | Footer progress bar đã được xóa chưa? | POS_UI-149 | | | |  |  |

---

## [POS_UI-150] C000105_お客様氏名
- Màn hình: C000105
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-150

**Feedback khách:**
> 、印刷担当者に修正をお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ Thông tin | Label đã đổi「販売担当者」→「印刷担当者」chưa? | POS_UI-150 | | | | M |  |

---

## [POS_UI-151] C000106_摘要入力
- Màn hình: C000106
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-151

**Feedback khách:**
> ×５行となります。
> ”MAX文字数入れたデザインの作成をお願いします。
> もし余白が余る場合は、調整をお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Input Fields & Form Design | Textbox đã thể hiện đúng spec 1行全角45文字×5行 chưa? | POS_UI-151 | | | | M |  |
| 2 | Input Fields & Form Design | Thiết kế đã có trường hợp MAX văn bản (45×5) chưa? | POS_UI-151 | | | | M |  |
| 3 | Cấu trúc Layout & Vị trí Thông tin | Layout đã được điều chỉnh nếu thừa khoảng trắng sau MAX text chưa? | POS_UI-151 | | | |  |  |

---

## [POS_UI-155] C000110_検索方法選択
- Màn hình: C000110
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-155

**Feedback khách:**
> 、以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-155 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment POS_UI-180 (C000123 cùng loại màn) đã được áp dụng đồng bộ chưa? | POS_UI-155 | | | |  |  |

---

## [POS_UI-157] C000111_未承認一覧表示
- Màn hình: C000111
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-157

**Feedback khách:**
> 。
> 以下コメントの
> 「・以下画像赤枠の機能ボタン（端末見積検索は除く）は引き継ぎたいので、ボタンを追加 または 別の手段で機能が実行できるようなデザインに修正」
> については、ボタン配置場所の検討を進めますので一旦保留でお願いいたします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Đã xác nhận yêu cầu thêm button (vùng đỏ) đang 保留 — chưa làm trong round này chưa? | POS_UI-157 | | | |  | Chờ khách confirm vị trí button |

---

## [POS_UI-158] C000114_詳細
- Màn hình: C000114
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-158

**Feedback khách:**
> 、その旨を表示しています。
> この仕様は引き継ぎたいため、デザインの追加をお願いします。
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ Thông tin | Trường hợp khách hàng không phải hội viên あんしんパスポート đã được thêm thông báo tương ứng (giống hiện hành) chưa? | POS_UI-158 | | | | M | Xem ảnh đính kèm trong ticket |

---

## [POS_UI-160] C000115_別紙内容確認
- Màn hình: C000115
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-160

**Feedback khách:**
> *(link)*
> 申し訳ございません。上記コメントについてです。
> 添付画像の画面「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加するデザインにしていただきますようお願いします。
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-160 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Tab「別紙内容確認」đã được thêm vào màn C000114_詳細 chưa? | POS_UI-160 | | | | M | Xem ảnh đính kèm |

---

## [POS_UI-161] C000116_次回訪問予定
- Màn hình: C000116
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-161

**Feedback khách:**
> 。
> *(link)*
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-161 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Tab「次回訪問予定」đã được thêm vào màn C000114_詳細 chưa? | POS_UI-161 | | | | M |  |

---

## [POS_UI-162] C000117_見積内容
- Màn hình: C000117
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-162

**Feedback khách:**
> 。
> *(link)*
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-162 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Tab「見積内容」đã được thêm vào màn C000114_詳細 chưa? | POS_UI-162 | | | | M |  |

---

## [POS_UI-163] C000118_見積結果
- Màn hình: C000118
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-163

**Feedback khách:**
> 。
> *(link)*
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-163 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Tab「見積結果」đã được thêm vào màn C000114_詳細 chưa? | POS_UI-163 | | | | M |  |

---

## [POS_UI-165] C000120_店舗への連絡
- Màn hình: C000120
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-165

**Feedback khách:**
> 。
> *(link)*
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-165 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Tab「店舗への連絡」đã được thêm vào màn C000114_詳細 chưa? | POS_UI-165 | | | | M |  |

---

## [POS_UI-166] C000121_コメント
- Màn hình: C000121
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-166

**Feedback khách:**
> 。
> *(link)*
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-166 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Tab「コメント」đã được thêm vào màn C000114_詳細 chưa? | POS_UI-166 | | | | M |  |

---

## [POS_UI-167] C000185_明細入力
- Màn hình: C000185
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-167

**Feedback khách:**
> 。
> *(ảnh đính kèm)*
> ・型番の文字数が少ないと思います。
> 表形式ではなく、売上と同じカード形式としていただきますようお願いします。
> ・このメニューは1取引3明細までとなりますので3明細分は表示できるよう調整をお願いします。
> ・”...”を表示する箇所はツールチップを表示する認識です。ツールチップの表示を含めたデザインの作成をお願いします。
> ・型番での検索も可能ですので、型番検索ボタン または 他の手段をデザインに反映をお願いします。
> ・「取消」を「在庫予約を取消」に修正をお願いします。
> また、「取消」は戻る系のボタンになりますので、左側に配置をお願いします。
> ・予約を試みたが、在庫がない場合はNo１のような表示になりますので、こちらのデザイン作成をお願いします。
> 作成後は、本チケットに添付をお願いします。
> *(ảnh đính kèm)*
> *(ảnh đính kèm)*
> ・在庫予約番号はレシートのバーコードをスキャンすることも想定されるため、カメラボタンの追加をお願いします。
> ・手入力時はキーボードを表示することになるかと思います。
> 手入力時のイメージをいただきたいため、キーボードが表示された場合のデザイン作成をお願いします。
> ・ボタンサイズが大きすぎるため、入力UIではなく選択UIのように見えてしまいます。
> テキストボックス、ボタンのサイズバランスについて、調整をお願いします。
> ・タイトルとラベルで「在庫予約番号」という文言が重複しているため、タイトルを削除 または ラベルを削除 どちらかを対応いただきたいです。
> *(ảnh đính kèm)*
> ・DC在庫予約と同じで明細のデザインはカード式でお願いします。
> ただ、明細の登録がないため、配送情報変更のようなデザインになるかと思います。
> *(ảnh đính kèm)*
> ・「進む」→「取消」に修正をお願いします。
> ・取消の場合は数量も表示しますので、デザインに反映をお願いします。（以下画像赤枠を参考）
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Cấu trúc Layout & Vị trí Thông tin | Hiển thị 明細 đã đổi từ 表形式 sang カード形式 (giống màn 売上) chưa? | POS_UI-167 | | | | M | Lý do: 型番 quá ngắn khi dùng bảng |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Tối đa 3 明細/giao dịch đã có đủ không gian hiển thị chưa? | POS_UI-167 | | | | M |  |
| 3 | UI Components & Controls | Tooltip đã được thêm cho các vị trí hiển thị「...」chưa? | POS_UI-167 | | | |  |  |
| 4 | Input Fields & Form Design | Chức năng tìm kiếm theo 型番 đã có button hoặc giải pháp khác chưa? | POS_UI-167 | | | |  |  |
| 5 | UI Components & Controls | Button「取消」đã đổi tên thành「在庫予約を取消」chưa? | POS_UI-167 | | | | M |  |
| 6 | Cấu trúc Layout & Vị trí Thông tin | Button「在庫予約を取消」(戻る系) đã được đặt ở bên trái chưa? | POS_UI-167 | | | |  |  |
| 7 | Hiển thị & Đồng bộ Thông tin | Thiết kế trường hợp không có tồn kho (在庫なし / No1) đã được tạo chưa? | POS_UI-167 | | | |  |  |

---

## [POS_UI-169] C000186_在庫引当確認 / 予約取消確認
- Màn hình: C000186
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-169

**Feedback khách:**
> 。
> ・本来伝えなければならない”DC在庫引当を行いますか。”のフォントサイズが小さく目立たない印象ですので、フォントサイズを上げて下さい。
> また、タイトルと本文で同じ内容かと思いますのでタイトルを削除し、本文は「DC在庫の引当を行いますか。」としてください
> ・選択肢は「いいえ」「はい」としてください。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Font size của「DC在庫の引当を行いますか。」đã đủ lớn và nổi bật chưa? | POS_UI-169 | | | |  | Hiện tại nhỏ, khó thấy |
| 2 | Header & Navigation | Tiêu đề trùng nội dung body đã được xóa chưa? | POS_UI-169 | | | |  |  |
| 3 | Hiển thị & Đồng bộ Thông tin | Body text đã sửa thành「DC在庫の引当を行いますか。」chưa? | POS_UI-169 | | | | M |  |
| 4 | UI Components & Controls | Lựa chọn đã đổi thành「いいえ」「はい」chưa? | POS_UI-169 | | | | M |  |

---

## [POS_UI-171] C000176_空き状況一覧表示
- Màn hình: C000176
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-14
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-171

**Feedback khách:**
> 。
> ・「センター店」表示エリアの"９１１２:試験配送センター"ですが、左側の表示エリアに"011-9112"（法人-店舗コード）が表示されているため、
> 店舗名のみの表示でお願いします。
> また、店舗名は最大全角16文字ですので、そちらを考慮した表示幅にしてください。
> 表示するデータも最大文字数としてください。
> ・前週 今週 翌週 の切替ですが、現在は以下の仕様となっております
> →現在表示している情報が今週の場合は「前週」の切替不可
> →1年以上先の情報も確認できるよう、「翌週」は1週間先のみではない（例：当営業日は2026/5/14の場合、2027/6/14 先も確認可能）
> ですので、これを踏まえたデザインの作成をお願いします。
> ・"エリア" が "アリア" になっているので、"エリア"に修正をお願いします。
> ・枠数は最大3桁(999)ですので、表示データは3桁表示でお願いします。
> ・予約処理ボタンがありません。
> また、本機能はエリアと日付を選択し、「予約処理」ボタンを押すと予約画面に映ります。
> このデザインですと、エリアと日付が押せるのかが分かりにくいと考えられます。
> デザインの修正、または 別の予約手段があればご提示をお願いします。
> ・Web受注ボタンを押した場合は、Web受注番号の入力に移るようにしていただきたいです。
> ・Web受注ボタンの表示有無は店舗によって変わりますので、表示がないバージョンのデザイン策k姓をお願いします。
> ※店舗がWeb通販店であれば表示、でなければ非表示
> ・取消ボタンは戻る系ですので、左側（戻るボタンの右側）に配置をお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ Thông tin | Vùng「センター店」đã chỉ hiển thị 店舗名 (không kèm 法人-店舗コード đã có ở vùng trái) chưa? | POS_UI-171 | | | | M |  |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Độ rộng cột 店舗名 đã tính đến tối đa 全角16文字 chưa? Dữ liệu mẫu đã dùng chuỗi tối đa chưa? | POS_UI-171 | | | |  |  |
| 3 | Screen Flow & Luồng Xử lý | Chức năng 前週/今週/翌週 đã phản ánh đúng spec chưa? (今週 → 前週 disabled; 翌週 xem được hơn 1 năm) | POS_UI-171 | | | |  |  |
| 4 | Hiển thị & Đồng bộ Thông tin | Lỗi chính tả「アリア」đã sửa thành「エリア」chưa? | POS_UI-171 | | | | M |  |

---

## [POS_UI-173] C000178_配送工事区分選択
- Màn hình: C000178
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-173

**Feedback khách:**
> 、配送情報変更_時間帯選択にデザインを合わせてください。
> *(ảnh đính kèm)*
> ・工事重み（数値）を入力する際キーボードが表示されると思いますので、キーボードを表示させたデザインの作成もお願いします。
> ・時間帯の件数が０件の場合は0/10の表記で、ボタンの状態は非活性となり押せない挙動になります。
> こちらのデザインについても作成をお願いします。
> また、他メニューでも同じ画面がありましたら合わせて対応をお願いします。
> ・ガイドメッセージが予約担当者入力時の内容ですので、画面に合わせた内容に修正をお願いします。
> ・エリアは店舗コード、店舗名ではなく、配送や工事エリア（水戸やいわき など）になりますので、デザインに反映をお願いします。
> ・本機能は「配送工事費予約」と統合されており、当該機能には予約画面でエリアの説明コメントを表示しております。
> なので、コメントの表示エリアをデザインに反映をお願いします。
> 表示コメントは全角５０文字×２行になります。
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Thiết kế button 時間帯 đã được đồng bộ theo chuẩn màn 配送情報変更_時間帯選択 chưa? | POS_UI-173 | | | | M |  |
| 2 | Input Fields & Form Design | Thiết kế màn hình khi keyboard hiển thị (lúc nhập 工事重み) đã được tạo chưa? | POS_UI-173 | | | |  |  |
| 3 | UI Components & Controls | Khi 時間帯 = 0件, đã hiển thị「0/10」và button 非活性 chưa? | POS_UI-173 | | | |  |  |
| 4 | Header & Navigation | Guide message đã được cập nhật phù hợp với màn này (không dùng guide của 予約担当者入力) chưa? | POS_UI-173 | | | |  |  |
| 5 | Hiển thị & Đồng bộ Thông tin | Vùng「エリア」đã hiển thị tên khu vực giao hàng/công trình (水戸, いわき...) thay vì 店舗コード chưa? | POS_UI-173 | | | | M |  |

---

## [POS_UI-174] C000180_指定方法選択
- Màn hình: C000180
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-174

**Feedback khách:**
> "指定方法"という単語が２回出てくるため、過剰に思います。※一部検索方法になっている
> ですので、タイトル：指定方法を選択は残して置き、「～を選択してください」のガイドは削除してください。
> 緑背景の検索方法も削除でお願いします。
> また、閉じるボタンと検索方法のボタンの幅が同じため、ぱっと見で３択に見えます。
> 閉じるボタンのサイズは他画面に合わせてください。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Guide「～を選択してください」và vùng xanh lá「検索方法」đã được xóa chưa? (từ「指定方法」đã có trong tiêu đề rồi) | POS_UI-174 | | | |  |  |
| 2 | UI Components & Controls | Kích thước button「閉じる」đã được thu nhỏ khớp với các màn khác chưa? | POS_UI-174 | | | |  | Hiện cùng size với button chính → trông như 3 lựa chọn |

---

## [POS_UI-175] B0401エリア絞込
- Màn hình: B0401エリア絞込
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-175

**Feedback khách:**
> 。
> ・エリア名称は最大で全角３０文字なので、その文字数がゆとりある形で入る程度の列幅で問題ありません。
> そのうえで、サブフォームのサイズ調整をお願いします。
> ・同じデータが表示されることは想定していないため、表示データは各Noバラバラにしてください。
> ・スクロールバーが明細に被らないよう調整してください。
> ・ボタン名は「進む」ではなく、「確定」にしてください。
> また、申し訳ありませんが「特定エリア表示」ボタンは削除でお願いします。
> 本メニューでは、現在使用されていない機能のようです。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Cấu trúc Layout & Vị trí Thông tin | エリアコード đã được căn giữa (中央揃え) chưa? | POS_UI-175 | | | | M | Chuẩn: code → center |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Độ rộng cột エリア名称 đã đủ cho tối đa 全角30文字 với margin thoải mái chưa? | POS_UI-175 | | | |  |  |
| 3 | Cấu trúc Layout & Vị trí Thông tin | Kích thước subform đã được điều chỉnh sau khi sửa độ rộng cột chưa? | POS_UI-175 | | | |  |  |
| 4 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng đã có nội dung khác nhau chưa? | POS_UI-175 | | | |  |  |
| 5 | Cấu trúc Layout & Vị trí Thông tin | Scrollbar đã không đè lên vùng 明細 chưa? | POS_UI-175 | | | |  |  |
| 6 | UI Components & Controls | Button「進む」đã đổi thành「確定」chưa? | POS_UI-175 | | | | M |  |
| 7 | UI Components & Controls | Button「特定エリア表示」đã được xóa chưa? (chức năng không còn dùng) | POS_UI-175 | | | |  |  |

---

## [POS_UI-176] C000181_JISコード入力
- Màn hình: C000181
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-176

**Feedback khách:**
> ・JISコード入力のテキストボックスには検索後、何が表示されますでしょうか？
> →JISコードのみでしょうか？それとも、都道府県＋市まで表示されますでしょうか？
> →未入力状態だけでなく、入力済みの状態のデザインの作成をお願いします。
> ・JISコード、配送頻度は中央揃えにしてください。
> ・"頻度"の"頻"の漢字が間違っています。
> ・住所は"ミトミツクニ"ではなく、都道府県＋市の表示にしてください。
> ・データは各明細で別の内容にしてください。
> ・スクロールバーは明細に被らないよう調整をお願いします。
> ・この画面は現行の「配送工事エリア担当店舗照会」のデザインだと思われますが、認識合っておりますか？
> 合っている場合、「確定ボタン」は不要でお願いします。
> また、「印刷ボタン」を青いボタンにしてください。
> ・「宅配不可エリア」ボタンを押した後の画面デザイン作成をお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Input Fields & Form Design | Thiết kế trạng thái chưa nhập (未入力) đã có chưa? | POS_UI-176 | | | | M |  |
| 2 | Input Fields & Form Design | Thiết kế trạng thái đã nhập (入力済み) với địa chỉ「都道府県＋市」đã có chưa? | POS_UI-176 | | | | M |  |
| 3 | Cấu trúc Layout & Vị trí Thông tin | JISコード và 配送頻度 đã được căn giữa chưa? | POS_UI-176 | | | | M |  |
| 4 | Hiển thị & Đồng bộ Thông tin | Lỗi chữ Hán trong「頻度」đã sửa đúng chưa? | POS_UI-176 | | | | M |  |
| 5 | Hiển thị & Đồng bộ Thông tin | Địa chỉ đã hiển thị「都道府県＋市」thay vì「ミトミツクニ」chưa? | POS_UI-176 | | | | M |  |
| 6 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng đã có nội dung khác nhau chưa? | POS_UI-176 | | | |  |  |
| 7 | Cấu trúc Layout & Vị trí Thông tin | Scrollbar đã không đè lên vùng 明細 chưa? | POS_UI-176 | | | |  |  |
| 8 | UI Components & Controls | Button「確定」đã được xóa chưa? | POS_UI-176 | | | |  |  |
| 9 | UI Components & Controls | Button「印刷」đã đổi sang màu xanh chưa? | POS_UI-176 | | | |  |  |
| 10 | Screen Flow & Luồng Xử lý | Màn hình sau khi nhấn「宅配不可エリア」đã được thiết kế chưa? | POS_UI-176 | | | |  |  |

---

## [POS_UI-178] C000182_店舗情報入力
- Màn hình: C000182
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-13
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-178

**Feedback khách:**
> 、店舗検索のテキストボックスには検索後、何が表示されますでしょうか？
> →法人、店舗コードのみでしょうか？それとも、法人コードと法人名、店舗コードと店舗名でしょうか？
> →未入力状態だけでなく、入力済みの状態のデザインの作成をお願いします。
> ・JISコード、配送頻度は中央揃えにしてください。
> ・"頻度"の"頻"の漢字が間違っています。
> ・住所は"ミトミツクニ"ではなく、都道府県＋市の表示にしてください。
> ・データは各明細で別の内容にしてください。
> ・スクロールバーは明細に被らないよう調整をお願いします。
> ・この画面は現行の「配送工事エリア担当店舗照会」のデザインだと思われますが、認識合っておりますか？
> 合っている場合、「確定ボタン」は不要でお願いします。
> また、「印刷ボタン」を青いボタンにしてください。
> ・「宅配不可エリア」ボタンを押した後の画面デザイン作成をお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Input Fields & Form Design | Thiết kế trạng thái chưa nhập (未入力) đã có chưa? | POS_UI-178 | | | | M |  |
| 2 | Input Fields & Form Design | Thiết kế trạng thái đã nhập (入力済み) với địa chỉ「都道府県＋市」đã có chưa? | POS_UI-178 | | | | M |  |
| 3 | Cấu trúc Layout & Vị trí Thông tin | JISコード và 配送頻度 đã được căn giữa chưa? | POS_UI-178 | | | | M |  |
| 4 | Hiển thị & Đồng bộ Thông tin | Lỗi chữ Hán trong「頻度」đã sửa đúng chưa? | POS_UI-178 | | | | M |  |
| 5 | Hiển thị & Đồng bộ Thông tin | Địa chỉ đã hiển thị「都道府県＋市」thay vì「ミトミツクニ」chưa? | POS_UI-178 | | | | M |  |
| 6 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng đã có nội dung khác nhau chưa? | POS_UI-178 | | | |  |  |
| 7 | Cấu trúc Layout & Vị trí Thông tin | Scrollbar đã không đè lên vùng 明細 chưa? | POS_UI-178 | | | |  |  |
| 8 | UI Components & Controls | Button「確定」đã được xóa chưa? | POS_UI-178 | | | |  |  |
| 9 | UI Components & Controls | Button「印刷」đã đổi sang màu xanh chưa? | POS_UI-178 | | | |  |  |
| 10 | Screen Flow & Luồng Xử lý | Màn hình sau khi nhấn「宅配不可エリア」đã được thiết kế chưa? | POS_UI-178 | | | |  |  |

---

## [POS_UI-180] C000123_検索方法選択
- Màn hình: C000123
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-180

**Feedback khách:**
> 。
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・担当者画面に表示ではなく、白背景に選択画面を表示するデザインにできますでしょうか。
> 簡単なイメージになります。
> *(ảnh đính kèm)*
> ・"検索方法"という単語が３回出てくるため、過剰に思います。
> ですので、タイトル：検索方法選択、「～を選択してください」のガイドを削除。
> 緑背景＋囲み線は残して置き、緑背景の部分は”検索方法選択”という文言に修正をお願いします。
> また、「指定なし」を「指定せずに検索 」としてください。
> ・閉じるボタンと検索方法のボタンの幅が同じため、ぱっと見で３択に見えます。
> 閉じるボタンのサイズは他画面に合わせてください。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-180 | | | | M |  |
| 2 | Input Fields & Form Design | Popup đã dùng nền trắng (白背景), không đè lên màn 担当者 chưa? | POS_UI-180 | | | |  |  |
| 3 | Header & Navigation | Từ「検索方法」đã chỉ còn 1 lần; guide và vùng xanh trùng đã xóa chưa? | POS_UI-180 | | | |  |  |
| 4 | UI Components & Controls | Vùng xanh lá đã được sửa thành text「検索方法選択」chưa? | POS_UI-180 | | | |  |  |
| 5 | UI Components & Controls | Nút「指定なし」đã đổi thành「指定せずに検索」chưa? | POS_UI-180 | | | |  |  |
| 6 | UI Components & Controls | Kích thước button「閉じる」đã được thu nhỏ khớp màn khác chưa? | POS_UI-180 | | | |  | Hiện trông như 3 lựa chọn |

---

## [POS_UI-181] C000125_端末見積書検索サブフォーム
- Màn hình: C000125
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-181

**Feedback khách:**
> 「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-181 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment POS_UI-156 đã được áp dụng chưa? | POS_UI-181 | | | |  | Cần mở POS_UI-156 xem comment |

---

## [POS_UI-182] C000124_未承認一覧表示
- Màn hình: C000124
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-182

**Feedback khách:**
> 。
> ・本チケットのタイトルを「C000124_未印刷一覧表示」に修正をお願いします。
> ・タイトルは「見積書未印刷一覧（配送端末）」に修正
> ・選択列のヘッダーはチェックボックスコントロールを置かずに、文言"選択"にする
> ・以下画像赤枠の機能ボタンは引き継ぎたいので、ボタンを追加 または 別の手段で機能が実行できるようなデザインに修正
> *(ảnh đính kèm)*
> また、本機能は承認された見積書を印刷するメニューなので、青色ボタンは「印刷」にする
> ・スクロールバーが金額欄と重なっているため、重ならないように調整
> → 売上画面のスクロールバー仕様と異なっている
> ・サンプルとして表示する明細情報は、Noごとに異なる内容にする
> あわせて、ツールチップ表示のデザインを追加
> → 他画面についても同様に対応
> ・現行では1ページ18明細表示なので、可能な限り18明細に近い明細数を表示できるよう上下余白を調整

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-182 | | | | M |  |
| 2 | UI Components & Controls | Header cột '選択' đã dùng text「選択」thay vì checkbox control chưa? | POS_UI-182 | | | |  |  |
| 3 | UI Components & Controls | Các button chức năng (vùng đỏ trong ảnh) đã được thêm lại hoặc có giải pháp thay thế chưa? | POS_UI-182 | | | |  |  |
| 4 | UI Components & Controls | Button xanh đã được đặt tên「印刷」chưa? | POS_UI-182 | | | |  | Menu in 見積書 đã duyệt |
| 5 | Cấu trúc Layout & Vị trí Thông tin | Scrollbar đã không đè lên vùng 金額欄 chưa? | POS_UI-182 | | | |  |  |
| 6 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng đã có nội dung khác nhau chưa? | POS_UI-182 | | | |  |  |
| 7 | UI Components & Controls | Tooltip đã được thêm cho các vị trí hiển thị「...」chưa? | POS_UI-182 | | | |  |  |

---

## [POS_UI-183] C000127_詳細
- Màn hình: C000127
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-183

**Feedback khách:**
> 、その旨を表示しています。
> この仕様は引き継ぎたいため、デザインの追加をお願いします。
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-183 | | | | M |  |
| 2 | Hiển thị & Đồng bộ Thông tin | Trường hợp không phải hội viên あんしんパスポート đã được thêm thông báo tương ứng chưa? | POS_UI-183 | | | | M | Xem ảnh đính kèm |

---

## [POS_UI-184] C000126_印刷確認
- Màn hình: C000126
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-184

**Feedback khách:**
> 「お客様控えのみ」「会員番号記載」のみでは直感的に分かりにくいため、
> 「お客様控えのみを印刷」「見積書に会員番号を記載」に文言変更をお願いします。
> ・「C000124_未印刷一覧表示」で印刷をする場合、現行では以下のデザイン、流れになります。
> *(ảnh đính kèm)*
> ↓
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-184 | | | | M |  |
| 2 | UI Components & Controls | Text button đã đổi thành「お客様控えのみを印刷」chưa? | POS_UI-184 | | | | M | Từ cũ ngắn, không trực quan |
| 3 | UI Components & Controls | Text button đã đổi thành「見積書に会員番号を記載」chưa? | POS_UI-184 | | | | M |  |
| 4 | Screen Flow & Luồng Xử lý | Flow in từ màn「未印刷一覧表示」đã phản ánh đúng flow hiện hành (xem ảnh đính kèm) chưa? | POS_UI-184 | | | |  |  |

---

## [POS_UI-185] C000128_別紙内容確認
- Màn hình: C000128
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-185

**Feedback khách:**
> 「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-185 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment trong ticket đã được áp dụng chưa? | POS_UI-185 | | | |  |  |

---

## [POS_UI-186] C000129_次回訪問予定
- Màn hình: C000129
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-186

**Feedback khách:**
> 「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-186 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment trong ticket đã được áp dụng chưa? | POS_UI-186 | | | |  |  |

---

## [POS_UI-187] C000130_見積内容
- Màn hình: C000130
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-187

**Feedback khách:**
> 「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-187 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment trong ticket đã được áp dụng chưa? | POS_UI-187 | | | |  |  |

---

## [POS_UI-188] C000131_見積結果
- Màn hình: C000131
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-188

**Feedback khách:**
> 「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-188 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment trong ticket đã được áp dụng chưa? | POS_UI-188 | | | |  |  |

---

## [POS_UI-190] C000133_店舗への連絡
- Màn hình: C000133
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-190

**Feedback khách:**
> 「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-190 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment trong ticket đã được áp dụng chưa? | POS_UI-190 | | | |  |  |

---

## [POS_UI-191] C000134_コメント
- Màn hình: C000134
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-191

**Feedback khách:**
> 「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> *(link)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề đã đổi thành「見積書未印刷一覧（配送端末）」chưa? | POS_UI-191 | | | | M |  |
| 2 | Tab & Thông tin Chi tiết / Consistency | Các sửa đổi theo comment POS_UI-166 đã được áp dụng chưa? | POS_UI-191 | | | |  |  |

---

## [POS_UI-194] 返品エラー通知
- Màn hình: 返品エラー通知
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-194

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Tab & Thông tin Chi tiết / Consistency | *(Chưa có comment — cần mở Backlog xem comment gốc)* | POS_UI-194 | | | |  |  |

---

## [POS_UI-195] 元伝と新黒決済確認
- Màn hình: 元伝と新黒決済確認
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-195

**Feedback khách:**
> *(ảnh đính kèm)*
> ・お買上げ総数、総額については、最新のデザインに反映をお願いします。（画像赤枠）
> ・未決済金額について、デザインに反映をお願いします。（画像青枠）
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Hiển thị & Đồng bộ Thông tin | お買上げ総数・総額 đã được cập nhật theo design mới nhất chưa? (xem ảnh vùng đỏ) | POS_UI-195 | | | | M |  |
| 2 | Hiển thị & Đồng bộ Thông tin | 未決済金額 đã được thêm vào design chưa? (xem ảnh vùng xanh) | POS_UI-195 | | | | M |  |

---

## [POS_UI-196] C000058_決済種別変更の確認
- Màn hình: C000058
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-196

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Tab & Thông tin Chi tiết / Consistency | *(Chưa có comment — cần mở Backlog xem comment gốc)* | POS_UI-196 | | | |  |  |

---

## [POS_UI-197] 元伝カード決済引き継ぎの確認
- Màn hình: 元伝カード決済引き継ぎの確認
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-197

**Feedback khách:**
> 「元伝カード決済」のタイトルは削除でお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề「元伝カード決済」ở phía trên màn hình đã được xóa chưa? | POS_UI-197 | | | | M |  |

---

## [POS_UI-198] 元伝決済時カード持ち確認
- Màn hình: 元伝決済時カード持ち確認
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-198

**Feedback khách:**
> 「元伝決済時カード」のタイトルは削除でお願いします。
> ・「元伝決済時カード」を選択後は、自動で画面遷移する想定でしょうか。
> 確定ボタンのようなものがないため確認です。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Header & Navigation | Tiêu đề「元伝決済時カード」ở phía trên màn hình đã được xóa chưa? | POS_UI-198 | | | | M |  |
| 2 | Screen Flow & Luồng Xử lý | Spec chuyển màn sau khi chọn (tự động hay cần button?) đã được xác nhận với khách trước khi thiết kế chưa? | POS_UI-198 | | | |  | Hiện không có button xác nhận — cần hỏi khách |

---

## [POS_UI-201] C000047_客先配送予定日
- Màn hình: C000047
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-12
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-201

**Feedback khách:**
> 。
> *(ảnh đính kèm)*

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | UI Components & Controls | Thiết kế button 時間帯 đã được đồng bộ theo chuẩn màn 配送情報変更_時間帯選択 chưa? | POS_UI-201 | | | | M |  |

---

## [POS_UI-203] C000183_空き状況一覧表示
- Màn hình: C000183
- Người phụ trách: VTI アイン
- Ngày cập nhật: 2026-05-08
- Link Backlog: https://siconnect.backlog.com/view/POS_UI-203

**Feedback khách:**
> *(link)* と重複しているようです。（センター店名の表示がありません）
> 不要なチケットである可能性がありますので、ご確認をお願いします。

| # | Nhóm | Check Item | 出典 | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|---|---|
| 1 | Screen Flow & Luồng Xử lý | Ticket này đã được xác nhận là trùng với POS_UI-171 chưa? Nếu trùng → đóng ticket. | POS_UI-203 | | | |  | Khách đã comment: 重複している可能性あり |

---
