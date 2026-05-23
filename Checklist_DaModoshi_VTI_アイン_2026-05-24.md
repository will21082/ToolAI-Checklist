# Checklist 差戻／修正依頼 — VTI アイン

| Mục | Giá trị |
|---|---|
| Project | POS_UI — siconnect.backlog.com |
| Assignee | VTI アイン |
| Status | 30_差戻／修正依頼 |
| Tổng tickets | 45 |
| Ngày tổng hợp | 2026-05-24 |

---

## Tổng quan theo nhóm

| Nhóm | Số tickets |
|---|---|
| 💳 決済フロー系 (Luồng thanh toán) | 5 |
| 📦 配送・予約系 (Giao hàng / Đặt lịch) | 8 |
| 🧾 請求・決済系 (Hóa đơn / Thanh toán) | 11 |
| 📋 見積・承認系 (Báo giá / Phê duyệt) — Nhóm C000123-134 | 11 |
| 📋 見積・承認系 (Báo giá / Phê duyệt) — Nhóm C000110-121 | 9 |
| 🗺 エリア・検索系 (Khu vực / Tìm kiếm) | 1 |

---

## Tiến độ xử lý

| Key | Màn hình | Nội dung sửa | Hoàn thành | Ghi chú |
|---|---|---|---|---|
| POS_UI-139 | C000095_明細入力 |  | ☐ |  |
| POS_UI-140 | C000101_請求書一覧／納品書一覧表示 | @VTI アイン  ・Figmaの画面遷移図には請求書印刷の明細画面もありますので、こちらに添付をお願いします。 ・請求書、納品書印刷画面では商品明細の追加、削除、修正は行えません。 　商品明細が編集できない前提のデザインにしていただけますでしょうか。 | ☐ |  |
| POS_UI-148 | C000103_請求書日付 | @VTI アイン  以下修正をお願いします。 ・販売担当者ではなく、印刷担当者に修正 ・「元伝の決済」ラベルは不要 ・請求書発行時は日付が必ず決まっているので、「予定日未定」チェックボックスは削除 ・【請求書　印刷サンプル】の枠線で囲まれた～ の文は１行に収める ・【法求出 印刷サンプル】→【請求書 | ☐ |  |
| POS_UI-149 | C000104_お支払予定日 | @VTI アイン  以下修正をお願いします。 ・販売担当者ではなく、印刷担当者に修正 ・「お支払予定日」ラベル1つのみ表示 ・請求書発行時は日付が必ず決まっているので、「予定日未定」チェックボックスは削除 ・【請求書　印刷サンプル】の枠線で囲まれた～ の文は１行に収める ・【法求出 印刷サンプル】→ | ☐ |  |
| POS_UI-150 | C000105_お客様氏名 | @VTI アイン  販売担当者ではなく、印刷担当者に修正をお願いします。 | ☐ |  |
| POS_UI-151 | C000106_摘要入力 | @VTI アイン  摘要入力は1行全角４５文字×５行となります。 ”MAX文字数入れたデザインの作成をお願いします。 もし余白が余る場合は、調整をお願いします。 | ☐ |  |
| POS_UI-155 | C000110_検索方法選択 | @VTI アイン  五月雨式で申し訳ありませんが、以下コメントの対応をお願いします。 | ☐ |  |
| POS_UI-157 | C000111_未承認一覧表示 | @VTI アイン  申し訳ございません。 以下コメントの 「・以下画像赤枠の機能ボタン（端末見積検索は除く）は引き継ぎたいので、ボタンを追加 または 別の手段で機能が実行できるようなデザインに修正」 については、ボタン配置場所の検討を進めますので一旦保留でお願いいたします。 | ☐ |  |
| POS_UI-158 | C000114_詳細 | @VTI アイン  現行ではあんしんパスポート会員ではない顧客の見積書の場合は、その旨を表示しています。 この仕様は引き継ぎたいため、デザインの追加をお願いします。 [画像] | ☐ |  |
| POS_UI-160 | C000115_別紙内容確認 | @VTI アイン   申し訳ございません。上記コメントについてです。 添付画像の画面「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加するデザインにしていただきますようお願いします。 [画像] | ☐ |  |
| POS_UI-161 | C000116_次回訪問予定 | @VTI アイン  以下コメントの対応をお願いします。  「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。 | ☐ |  |
| POS_UI-162 | C000117_見積内容 | @VTI アイン  以下コメントの対応をお願いします。  「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。 | ☐ |  |
| POS_UI-163 | C000118_見積結果 | @VTI アイン  以下コメントの対応をお願いします。  「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。 | ☐ |  |
| POS_UI-165 | C000120_店舗への連絡 | @VTI アイン  以下コメントの対応をお願いします。  「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。 | ☐ |  |
| POS_UI-166 | C000121_コメント | @VTI アイン  以下コメントの対応をお願いします。  「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。 | ☐ |  |
| POS_UI-167 | C000185_明細入力 | @VTI アイン  以下修正をお願いします。 [画像] ・型番の文字数が少ないと思います。 　表形式ではなく、売上と同じカード形式としていただきますようお願いします。 ・このメニューは1取引3明細までとなりますので3明細分は表示できるよう調整をお願いします。 ・”...”を表示する箇所はツールチップ | ☐ |  |
| POS_UI-169 | C000186_在庫引当確認 / 予約取消確認 | @VTI アイン  以下修正をお願いします。 ・本来伝えなければならない”DC在庫引当を行いますか。”のフォントサイズが小さく目立たない印象ですので、フォントサイズを上げて下さい。 　また、タイトルと本文で同じ内容かと思いますのでタイトルを削除し、本文は「DC在庫の引当を行いますか。」としてください | ☐ |  |
| POS_UI-171 | C000176_空き状況一覧表示 | @VTI アイン  以下ご対応のほどよろしくお願いいたします。 ・「センター店」表示エリアの"９１１２:試験配送センター"ですが、左側の表示エリアに"011-9112"（法人-店舗コード）が表示されているため、 　店舗名のみの表示でお願いします。 　また、店舗名は最大全角16文字ですので、そちらを考 | ☐ |  |
| POS_UI-173 | C000178_配送工事区分選択 | @VTI アイン  ・時間帯の各ボタンデザインについては、配送情報変更_時間帯選択にデザインを合わせてください。 [画像]  ・工事重み（数値）を入力する際キーボードが表示されると思いますので、キーボードを表示させたデザインの作成もお願いします。  ・時間帯の件数が０件の場合は0/10の表記で、ボタ | ☐ |  |
| POS_UI-174 | C000180_指定方法選択 | @VTI アイン  "指定方法"という単語が２回出てくるため、過剰に思います。※一部検索方法になっている ですので、タイトル：指定方法を選択は残して置き、「～を選択してください」のガイドは削除してください。 緑背景の検索方法も削除でお願いします。 また、閉じるボタンと検索方法のボタンの幅が同じため、 | ☐ |  |
| POS_UI-175 | B0401エリア絞込 | @VTI アイン  ・エリアコードは中央揃えで表示してください。 ・エリア名称は最大で全角３０文字なので、その文字数がゆとりある形で入る程度の列幅で問題ありません。 　そのうえで、サブフォームのサイズ調整をお願いします。 ・同じデータが表示されることは想定していないため、表示データは各Noバラバラに | ☐ |  |
| POS_UI-176 | C000181_JISコード入力 | ・JISコード入力のテキストボックスには検索後、何が表示されますでしょうか？ 　→JISコードのみでしょうか？それとも、都道府県＋市まで表示されますでしょうか？ 　→未入力状態だけでなく、入力済みの状態のデザインの作成をお願いします。  ・JISコード、配送頻度は中央揃えにしてください。  ・"頻度 | ☐ |  |
| POS_UI-178 | C000182_店舗情報入力 | @VTI アイン  ・法人検索、店舗検索のテキストボックスには検索後、何が表示されますでしょうか？ 　→法人、店舗コードのみでしょうか？それとも、法人コードと法人名、店舗コードと店舗名でしょうか？ 　→未入力状態だけでなく、入力済みの状態のデザインの作成をお願いします。  ・JISコード、配送頻度は | ☐ |  |
| POS_UI-180 | C000123_検索方法選択 | @VTI アイン  以下検討をお願いします。 ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。 ・担当者画面に表示ではなく、白背景に選択画面を表示するデザインにできますでしょうか。 簡単なイメージになります。 [画像] ・"検索方法"という単語が３回出てくるため、過剰に思います。 　です | ☐ |  |
| POS_UI-181 | C000125_端末見積書検索サブフォーム | @VTI アイン  ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。 ・以下コメントの対応をお願いします。 | ☐ |  |
| POS_UI-182 | C000124_未承認一覧表示 | @VTI アイン  以下修正をお願いします。 ・本チケットのタイトルを「C000124_未印刷一覧表示」に修正をお願いします。 ・タイトルは「見積書未印刷一覧（配送端末）」に修正 ・選択列のヘッダーはチェックボックスコントロールを置かずに、文言"選択"にする ・以下画像赤枠の機能ボタンは引き継ぎたい | ☐ |  |
| POS_UI-183 | C000127_詳細 | @VTI アイン  現行ではあんしんパスポート会員ではない顧客の見積書の場合は、その旨を表示しています。 この仕様は引き継ぎたいため、デザインの追加をお願いします。 [画像] | ☐ |  |
| POS_UI-184 | C000126_印刷確認 | @VTI アイン  ・「お客様控えのみ」「会員番号記載」のみでは直感的に分かりにくいため、 「お客様控えのみを印刷」「見積書に会員番号を記載」に文言変更をお願いします。  ・「C000124_未印刷一覧表示」で印刷をする場合、現行では以下のデザイン、流れになります。 [画像] ↓ [画像] | ☐ |  |
| POS_UI-185 | C000128_別紙内容確認 | @VTI アイン  ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。 ・以下コメントの対応をお願いします。 | ☐ |  |
| POS_UI-186 | C000129_次回訪問予定 | @VTI アイン  ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。 ・以下コメントの対応をお願いします。 | ☐ |  |
| POS_UI-187 | C000130_見積内容 | @VTI アイン  ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。 ・以下コメントの対応をお願いします。 | ☐ |  |
| POS_UI-188 | C000131_見積結果 | @VTI アイン  ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。 ・以下コメントの対応をお願いします。 | ☐ |  |
| POS_UI-190 | C000133_店舗への連絡 | @VTI アイン  ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。 ・以下コメントの対応をお願いします。 | ☐ |  |
| POS_UI-191 | C000134_コメント | @VTI アイン  ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。 ・以下コメントの対応をお願いします。 | ☐ |  |
| POS_UI-194 | 返品エラー通知 |  | ☐ |  |
| POS_UI-195 | 元伝と新黒決済確認 | @VTI アイン  [画像] ・お買上げ総数、総額については、最新のデザインに反映をお願いします。（画像赤枠） ・未決済金額について、デザインに反映をお願いします。（画像青枠） [画像] | ☐ |  |
| POS_UI-196 | C000058_決済種別変更の確認 |  | ☐ |  |
| POS_UI-197 | 元伝カード決済引き継ぎの確認 | @VTI アイン  上に表示している「元伝カード決済」のタイトルは削除でお願いします。 | ☐ |  |
| POS_UI-198 | 元伝決済時カード持ち確認 | @VTI アイン  ・上に表示している「元伝決済時カード」のタイトルは削除でお願いします。 ・「元伝決済時カード」を選択後は、自動で画面遷移する想定でしょうか。 　確定ボタンのようなものがないため確認です。 | ☐ |  |
| POS_UI-201 | C000047_客先配送予定日 | @VTI アイン  配送情報変更_時間帯選択にデザインを合わせてください。 [画像] | ☐ |  |
| POS_UI-203 | C000183_空き状況一覧表示 | @VTI アイン   と重複しているようです。（センター店名の表示がありません） 不要なチケットである可能性がありますので、ご確認をお願いします。 | ☐ |  |
| POS_UI-69 | C000048_時間帯選択 | @VTI アイン  配送情報変更_時間帯選択にデザインを合わせてください。 [画像] | ☐ | ⚠️ 2026-03-31 |
| POS_UI-72 | C000052_別紙案内 |  | ☐ | ⚠️ 2026-03-31 |
| POS_UI-73 | C000053_お客様情報 | 以下コメントの対応をお願いします。 | ☐ | ⚠️ 2026-03-31 |
| POS_UI-82 | A0426_新黒伝決済（お預かり金額入力） | 他のメニューとデザインが異なりますので統一をお願いします。 | ☐ | ⚠️ 2026-03-31 |

---

## Checklist Chi tiết theo Nhóm

### 💳 決済フロー系 (Luồng thanh toán)  (5 tickets)

#### 1. [POS_UI-194] 返品エラー通知

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> *(Chưa có comment)*

#### 2. [POS_UI-195] 元伝と新黒決済確認

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> *(có đính kèm ảnh)*
> ・お買上げ総数、総額については、最新のデザインに反映をお願いします。（画像赤枠）
> ・未決済金額について、デザインに反映をお願いします。（画像青枠）
> *(có đính kèm ảnh)*

#### 3. [POS_UI-197] 元伝カード決済引き継ぎの確認

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 上に表示している「元伝カード決済」のタイトルは削除でお願いします。

#### 4. [POS_UI-198] 元伝決済時カード持ち確認

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・上に表示している「元伝決済時カード」のタイトルは削除でお願いします。
> ・「元伝決済時カード」を選択後は、自動で画面遷移する想定でしょうか。
> 　確定ボタンのようなものがないため確認です。

#### 5. [POS_UI-82] A0426_新黒伝決済（お預かり金額入力） · ⚠️ Due: **2026-03-31**

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> 他のメニューとデザインが異なりますので統一をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-18)

### 📦 配送・予約系 (Giao hàng / Đặt lịch)  (8 tickets)

#### 6. [POS_UI-167] C000185_明細入力

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下修正をお願いします。
> *(có đính kèm ảnh)*
> ・型番の文字数が少ないと思います。
> 　表形式ではなく、売上と同じカード形式としていただきますようお願いします。
> ・このメニューは1取引3明細までとなりますので3明細分は表示できるよう調整をお願いします。
> ・”...”を表示する箇所はツールチップを表示する認識です。ツールチップの表示を含めたデザインの作成をお願いします。
> ・型番での検索も可能ですので、型番検索ボタン または 他の手段をデザインに反映をお願いします。
> ・「取消」を「在庫予約を取消」に修正をお願いします。
> 　また、「取消」は戻る系のボタンになりますので、左側に配置をお願いします。
> ・予約を試みたが、在庫がない場合はNo１のような表示になりますので、こちらのデザイン作成をお願いします。
> 　作成後は、本チケットに添付をお願いします。
> *(có đính kèm ảnh)*
> 
> 
> *(có đính kèm ảnh)*
> ・在庫予約番号はレシートのバーコードをスキャンすることも想定されるため、カメラボタンの追加をお願いします。
> ・手入力時はキーボードを表示することになるかと思います。
> 　手入力時のイメージをいただきたいため、キーボードが表示された場合のデザイン作成をお願いします。
> ・ボタンサイズが大きすぎるため、入力UIではなく選択UIのように見えてしまいます。
> 　テキストボックス、ボタンのサイズバランスについて、調整をお願いします。
> ・タイトルとラベルで「在庫予約番号」という文言が重複しているため、タイトルを削除 または ラベルを削除 どちらかを対応いただきたいです。
> 
> 
> *(có đính kèm ảnh)*
> ・DC在庫予約と同じで明細のデザインはカード式でお願いします。
> 　ただ、明細の登録がないため、配送情報変更のようなデザインになるかと思います。
> *(có đính kèm ảnh)*
> ・「進む」→「取消」に修正をお願いします。
> ・取消の場合は数量も表示しますので、デザインに反映をお願いします。（以下画像赤枠を参考）
> *(có đính kèm ảnh)*

#### 7. [POS_UI-169] C000186_在庫引当確認 / 予約取消確認

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下修正をお願いします。
> ・本来伝えなければならない”DC在庫引当を行いますか。”のフォントサイズが小さく目立たない印象ですので、フォントサイズを上げて下さい。
> 　また、タイトルと本文で同じ内容かと思いますのでタイトルを削除し、本文は「DC在庫の引当を行いますか。」としてください
> ・選択肢は「いいえ」「はい」としてください。

#### 8. [POS_UI-171] C000176_空き状況一覧表示

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下ご対応のほどよろしくお願いいたします。
> ・「センター店」表示エリアの"９１１２:試験配送センター"ですが、左側の表示エリアに"011-9112"（法人-店舗コード）が表示されているため、
> 　店舗名のみの表示でお願いします。
> 　また、店舗名は最大全角16文字ですので、そちらを考慮した表示幅にしてください。
> 　表示するデータも最大文字数としてください。
> 
> ・前週 今週 翌週 の切替ですが、現在は以下の仕様となっております
> 　→現在表示している情報が今週の場合は「前週」の切替不可
> 　→1年以上先の情報も確認できるよう、「翌週」は1週間先のみではない（例：当営業日は2026/5/14の場合、2027/6/14 先も確認可能）
> 　ですので、これを踏まえたデザインの作成をお願いします。
> 
> ・"エリア" が "アリア" になっているので、"エリア"に修正をお願いします。
> 
> ・枠数は最大3桁(999)ですので、表示データは3桁表示でお願いします。
> 
> ・予約処理ボタンがありません。
> 　また、本機能はエリアと日付を選択し、「予約処理」ボタンを押すと予約画面に映ります。
> 　このデザインですと、エリアと日付が押せるのかが分かりにくいと考えられます。
> 　デザインの修正、または 別の予約手段があればご提示をお願いします。
> 
> ・Web受注ボタンを押した場合は、Web受注番号の入力に移るようにしていただきたいです。
> 
> ・Web受注ボタンの表示有無は店舗によって変わりますので、表示がないバージョンのデザイン策k姓をお願いします。
> 　※店舗がWeb通販店であれば表示、でなければ非表示
> 
> ・取消ボタンは戻る系ですので、左側（戻るボタンの右側）に配置をお願いします。

#### 9. [POS_UI-173] C000178_配送工事区分選択

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・時間帯の各ボタンデザインについては、配送情報変更_時間帯選択にデザインを合わせてください。
> *(có đính kèm ảnh)*
> 
> ・工事重み（数値）を入力する際キーボードが表示されると思いますので、キーボードを表示させたデザインの作成もお願いします。
> 
> ・時間帯の件数が０件の場合は0/10の表記で、ボタンの状態は非活性となり押せない挙動になります。
> 　こちらのデザインについても作成をお願いします。
> 　また、他メニューでも同じ画面がありましたら合わせて対応をお願いします。
> 
> ・ガイドメッセージが予約担当者入力時の内容ですので、画面に合わせた内容に修正をお願いします。
> 
> ・エリアは店舗コード、店舗名ではなく、配送や工事エリア（水戸やいわき など）になりますので、デザインに反映をお願いします。
> 
> ・本機能は「配送工事費予約」と統合されており、当該機能には予約画面でエリアの説明コメントを表示しております。
> 　なので、コメントの表示エリアをデザインに反映をお願いします。
> 　表示コメントは全角５０文字×２行になります。
> *(có đính kèm ảnh)*

#### 10. [POS_UI-174] C000180_指定方法選択

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> "指定方法"という単語が２回出てくるため、過剰に思います。※一部検索方法になっている
> ですので、タイトル：指定方法を選択は残して置き、「～を選択してください」のガイドは削除してください。
> 緑背景の検索方法も削除でお願いします。
> また、閉じるボタンと検索方法のボタンの幅が同じため、ぱっと見で３択に見えます。
> 閉じるボタンのサイズは他画面に合わせてください。

#### 11. [POS_UI-176] C000181_JISコード入力

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> ・JISコード入力のテキストボックスには検索後、何が表示されますでしょうか？
> 　→JISコードのみでしょうか？それとも、都道府県＋市まで表示されますでしょうか？
> 　→未入力状態だけでなく、入力済みの状態のデザインの作成をお願いします。
> 
> ・JISコード、配送頻度は中央揃えにしてください。
> 
> ・"頻度"の"頻"の漢字が間違っています。
> 
> ・住所は"ミトミツクニ"ではなく、都道府県＋市の表示にしてください。
> 
> ・データは各明細で別の内容にしてください。
> 
> ・スクロールバーは明細に被らないよう調整をお願いします。
> 
> ・この画面は現行の「配送工事エリア担当店舗照会」のデザインだと思われますが、認識合っておりますか？
> 　合っている場合、「確定ボタン」は不要でお願いします。
> 　また、「印刷ボタン」を青いボタンにしてください。
> 
> ・「宅配不可エリア」ボタンを押した後の画面デザイン作成をお願いします。

#### 12. [POS_UI-178] C000182_店舗情報入力

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・法人検索、店舗検索のテキストボックスには検索後、何が表示されますでしょうか？
> 　→法人、店舗コードのみでしょうか？それとも、法人コードと法人名、店舗コードと店舗名でしょうか？
> 　→未入力状態だけでなく、入力済みの状態のデザインの作成をお願いします。
> 
> ・JISコード、配送頻度は中央揃えにしてください。
> 
> ・"頻度"の"頻"の漢字が間違っています。
> 
> ・住所は"ミトミツクニ"ではなく、都道府県＋市の表示にしてください。
> 
> ・データは各明細で別の内容にしてください。
> 
> ・スクロールバーは明細に被らないよう調整をお願いします。
> 
> ・この画面は現行の「配送工事エリア担当店舗照会」のデザインだと思われますが、認識合っておりますか？
> 　合っている場合、「確定ボタン」は不要でお願いします。
> 　また、「印刷ボタン」を青いボタンにしてください。
> 
> ・「宅配不可エリア」ボタンを押した後の画面デザイン作成をお願いします。

#### 13. [POS_UI-203] C000183_空き状況一覧表示

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> [link](https://siconnect.backlog.com/view/POS_UI-171) と重複しているようです。（センター店名の表示がありません）
> 不要なチケットである可能性がありますので、ご確認をお願いします。

### 🧾 請求・決済系 (Hóa đơn / Thanh toán)  (11 tickets)

#### 14. [POS_UI-139] C000095_明細入力

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> *(Chưa có comment)*

#### 15. [POS_UI-140] C000101_請求書一覧／納品書一覧表示

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・Figmaの画面遷移図には請求書印刷の明細画面もありますので、こちらに添付をお願いします。
> ・請求書、納品書印刷画面では商品明細の追加、削除、修正は行えません。
> 　商品明細が編集できない前提のデザインにしていただけますでしょうか。

#### 16. [POS_UI-148] C000103_請求書日付

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下修正をお願いします。
> ・販売担当者ではなく、印刷担当者に修正
> ・「元伝の決済」ラベルは不要
> ・請求書発行時は日付が必ず決まっているので、「予定日未定」チェックボックスは削除
> ・【請求書　印刷サンプル】の枠線で囲まれた～ の文は１行に収める
> ・【法求出 印刷サンプル】→【請求書　印刷サンプル】に修正
> ・文言の位置は以下画像に合わせる
> *(có đính kèm ảnh)*
> ・フッターの進捗バーは不要
> ※既成のデザインを流用いただくのは問題ありませんが、現行画面を見比べていただきますようお願いいたします。

#### 17. [POS_UI-149] C000104_お支払予定日

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下修正をお願いします。
> ・販売担当者ではなく、印刷担当者に修正
> ・「お支払予定日」ラベル1つのみ表示
> ・請求書発行時は日付が必ず決まっているので、「予定日未定」チェックボックスは削除
> ・【請求書　印刷サンプル】の枠線で囲まれた～ の文は１行に収める
> ・【法求出 印刷サンプル】→【請求書　印刷サンプル】に修正
> ・赤枠の位置が違います。添付画像青枠の位置にする
> *(có đính kèm ảnh)*
> ・文言の位置は以下画像に合わせる
> *(có đính kèm ảnh)*
> ・フッターの進捗バーは不要
> ※既成のデザインを流用いただくのは問題ありませんが、現行画面を見比べていただきますようお願いいたします。

#### 18. [POS_UI-150] C000105_お客様氏名

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 販売担当者ではなく、印刷担当者に修正をお願いします。

#### 19. [POS_UI-151] C000106_摘要入力

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 摘要入力は1行全角４５文字×５行となります。
> ”MAX文字数入れたデザインの作成をお願いします。
> もし余白が余る場合は、調整をお願いします。

#### 20. [POS_UI-196] C000058_決済種別変更の確認

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> *(Chưa có comment)*

#### 21. [POS_UI-201] C000047_客先配送予定日

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 配送情報変更_時間帯選択にデザインを合わせてください。
> *(có đính kèm ảnh)*

#### 22. [POS_UI-69] C000048_時間帯選択 · ⚠️ Due: **2026-03-31**

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 配送情報変更_時間帯選択にデザインを合わせてください。
> *(có đính kèm ảnh)*

#### 23. [POS_UI-72] C000052_別紙案内 · ⚠️ Due: **2026-03-31**

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> *(Chưa có comment)*

#### 24. [POS_UI-73] C000053_お客様情報 · ⚠️ Due: **2026-03-31**

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> 以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-40#comment-721884429)

### 📋 見積・承認系 (Báo giá / Phê duyệt) — Nhóm C000123-134  (11 tickets)

#### 25. [POS_UI-180] C000123_検索方法選択

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下検討をお願いします。
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・担当者画面に表示ではなく、白背景に選択画面を表示するデザインにできますでしょうか。
> 簡単なイメージになります。
> *(có đính kèm ảnh)*
> ・"検索方法"という単語が３回出てくるため、過剰に思います。
> 　ですので、タイトル：検索方法選択、「～を選択してください」のガイドを削除。
> 　緑背景＋囲み線は残して置き、緑背景の部分は”検索方法選択”という文言に修正をお願いします。
> 　また、「指定なし」を「指定せずに検索 」としてください。
> ・閉じるボタンと検索方法のボタンの幅が同じため、ぱっと見で３択に見えます。
> 　閉じるボタンのサイズは他画面に合わせてください。

#### 26. [POS_UI-181] C000125_端末見積書検索サブフォーム

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-156#comment-732589585)

#### 27. [POS_UI-182] C000124_未承認一覧表示

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下修正をお願いします。
> ・本チケットのタイトルを「C000124_未印刷一覧表示」に修正をお願いします。
> ・タイトルは「見積書未印刷一覧（配送端末）」に修正
> ・選択列のヘッダーはチェックボックスコントロールを置かずに、文言"選択"にする
> ・以下画像赤枠の機能ボタンは引き継ぎたいので、ボタンを追加 または 別の手段で機能が実行できるようなデザインに修正
> *(có đính kèm ảnh)*
> 　また、本機能は承認された見積書を印刷するメニューなので、青色ボタンは「印刷」にする
> ・スクロールバーが金額欄と重なっているため、重ならないように調整
> 　→ 売上画面のスクロールバー仕様と異なっている
> ・サンプルとして表示する明細情報は、Noごとに異なる内容にする
> 　あわせて、ツールチップ表示のデザインを追加
> 　→ 他画面についても同様に対応
> ・現行では1ページ18明細表示なので、可能な限り18明細に近い明細数を表示できるよう上下余白を調整

#### 28. [POS_UI-183] C000127_詳細

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 現行ではあんしんパスポート会員ではない顧客の見積書の場合は、その旨を表示しています。
> この仕様は引き継ぎたいため、デザインの追加をお願いします。
> *(có đính kèm ảnh)*

#### 29. [POS_UI-184] C000126_印刷確認

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・「お客様控えのみ」「会員番号記載」のみでは直感的に分かりにくいため、
> 「お客様控えのみを印刷」「見積書に会員番号を記載」に文言変更をお願いします。
> 
> ・「C000124_未印刷一覧表示」で印刷をする場合、現行では以下のデザイン、流れになります。
> *(có đính kèm ảnh)*
> ↓
> *(có đính kèm ảnh)*

#### 30. [POS_UI-185] C000128_別紙内容確認

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-160#comment-734882594)

#### 31. [POS_UI-186] C000129_次回訪問予定

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-161#comment-734888361)

#### 32. [POS_UI-187] C000130_見積内容

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-162#comment-734913270)

#### 33. [POS_UI-188] C000131_見積結果

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-163#comment-734915564)

#### 34. [POS_UI-190] C000133_店舗への連絡

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-164#comment-734921550)

#### 35. [POS_UI-191] C000134_コメント

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・タイトルは「見積書未印刷一覧（配送端末）」でお願いします。
> ・以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-166#comment-734924654)

### 📋 見積・承認系 (Báo giá / Phê duyệt) — Nhóm C000110-121  (9 tickets)

#### 36. [POS_UI-155] C000110_検索方法選択

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 五月雨式で申し訳ありませんが、以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-180#comment-734964609)

#### 37. [POS_UI-157] C000111_未承認一覧表示

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 申し訳ございません。
> 以下コメントの
> 「・以下画像赤枠の機能ボタン（端末見積検索は除く）は引き継ぎたいので、ボタンを追加 または 別の手段で機能が実行できるようなデザインに修正」
> については、ボタン配置場所の検討を進めますので一旦保留でお願いいたします。
> [link](https://siconnect.backlog.com/view/POS_UI-157#comment-734851135)

#### 38. [POS_UI-158] C000114_詳細

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 現行ではあんしんパスポート会員ではない顧客の見積書の場合は、その旨を表示しています。
> この仕様は引き継ぎたいため、デザインの追加をお願いします。
> *(có đính kèm ảnh)*

#### 39. [POS_UI-160] C000115_別紙内容確認

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> [link](https://siconnect.backlog.com/view/POS_UI-160#comment-734882594)
> 申し訳ございません。上記コメントについてです。
> 添付画像の画面「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加するデザインにしていただきますようお願いします。
> *(có đính kèm ảnh)*

#### 40. [POS_UI-161] C000116_次回訪問予定

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-160#comment-736195478)
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

#### 41. [POS_UI-162] C000117_見積内容

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-160#comment-736195478)
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

#### 42. [POS_UI-163] C000118_見積結果

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-160#comment-736195478)
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

#### 43. [POS_UI-165] C000120_店舗への連絡

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-160#comment-736195478)
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

#### 44. [POS_UI-166] C000121_コメント

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> 以下コメントの対応をお願いします。
> [link](https://siconnect.backlog.com/view/POS_UI-160#comment-736195478)
> 「C000114_詳細」に、「次回訪問予定」～「コメント」のタブを追加したデザインにしていただきますようお願いします。

### 🗺 エリア・検索系 (Khu vực / Tìm kiếm)  (1 tickets)

#### 45. [POS_UI-175] B0401エリア絞込

- [ ] Đọc feedback và hiểu yêu cầu sửa
- [ ] Thực hiện sửa thiết kế
- [ ] Self-review theo checklist POS_UI guideline
- [ ] Upload bản sửa lên Backlog
- [ ] Cập nhật status → 20_確認待ち

> **Feedback từ khách:**
> @VTI アイン 
> ・エリアコードは中央揃えで表示してください。
> ・エリア名称は最大で全角３０文字なので、その文字数がゆとりある形で入る程度の列幅で問題ありません。
> 　そのうえで、サブフォームのサイズ調整をお願いします。
> ・同じデータが表示されることは想定していないため、表示データは各Noバラバラにしてください。
> ・スクロールバーが明細に被らないよう調整してください。
> ・ボタン名は「進む」ではなく、「確定」にしてください。
> 
> また、申し訳ありませんが「特定エリア表示」ボタンは削除でお願いします。
> 本メニューでは、現在使用されていない機能のようです。
