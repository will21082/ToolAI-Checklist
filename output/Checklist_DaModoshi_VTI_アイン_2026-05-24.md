# SHARP POS UI — Design Review Checklist
> VTI アイン · 30_差戻／修正依頼 · 2026-05-24 · Chuẩn: Checklist_Screen_Design_VN.md

| | |
|---|---|
| Tổng tickets | 38 |
| Tổng việc cần sửa | ~180 |
| Khoảng ngày comment | 2026-05-08 ～ 2026-05-14 |
| Điều kiện lọc | assignee = VTI アイン · status = 30_差戻／修正依頼 |

**Cách dùng:** Sửa xong từng dòng → điền `OK` / `NOK` / `N/A` vào Round 1 → khi tất cả OK → upload → đổi status Backlog `20_確認待ち`.

---

## [POS_UI-148] C000103_請求書日付
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Đổi label「販売担当者」thành「印刷担当者」 | c-734823143 | | | | | |
| 2 | Hiển thị & Đồng bộ Thông tin | Xóa label「元伝の決済」 | c-734823143 | | | | | |
| 3 | Input Fields & Form Design | Xóa checkbox「予定日未定」(ngày luôn xác định khi in hóa đơn) | c-734823143 | | | | | |
| 4 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề in mẫu từ「法求出 印刷サンプル」thành「請求書　印刷サンプル」 | c-734823143 | | | | | Lỗi typo |
| 5 | Cấu trúc Layout & Vị trí Thông tin | Thu gọn văn bản trong khung viền thành 1 dòng | c-734823143 | | | | | |
| 6 | Cấu trúc Layout & Vị trí Thông tin | Căn chỉnh vị trí văn bản theo ảnh đính kèm | c-734823143 | | | | | |
| 7 | Header & Navigation | Xóa progress bar (stepbar) ở footer | c-734823143 | | | | | |

---

## [POS_UI-149] C000104_お支払予定日
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Đổi label「販売担当者」thành「印刷担当者」 | c-734830032 | | | | | |
| 2 | Hiển thị & Đồng bộ Thông tin | Chỉ hiển thị 1 label「お支払予定日」(bỏ label trùng) | c-734830032 | | | | | |
| 3 | Input Fields & Form Design | Xóa checkbox「予定日未定」 | c-734830032 | | | | | |
| 4 | Cấu trúc Layout & Vị trí Thông tin | Thu gọn văn bản trong khung viền thành 1 dòng | c-734830032 | | | | | |
| 5 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề in mẫu từ「法求出 印刷サンプル」thành「請求書　印刷サンプル」 | c-734830032 | | | | | Lỗi typo |
| 6 | Cấu trúc Layout & Vị trí Thông tin | Di chuyển vùng đóng khung (hiện ở vị trí đỏ) sang vị trí xanh theo ảnh đính kèm | c-734830032 | | | | | |
| 7 | Cấu trúc Layout & Vị trí Thông tin | Căn chỉnh vị trí văn bản theo ảnh đính kèm | c-734830032 | | | | | |
| 8 | Header & Navigation | Xóa progress bar (stepbar) ở footer | c-734830032 | | | | | |

---

## [POS_UI-150] C000105_お客様氏名
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Đổi label「販売担当者」thành「印刷担当者」 | c-734833527 | | | | | |

---

## [POS_UI-151] C000106_摘要入力
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Input Fields & Form Design | Tạo thiết kế ô nhập摘要với nội dung MAX (1 dòng tối đa 45 ký tự toàn giác × 5 dòng); điều chỉnh khoảng trắng trên/dưới nếu còn thừa | c-734835303 | | | | | |

---

## [POS_UI-155] C000110_検索方法選択
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 ～ 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Screen Flow & Luồng Xử lý | Thay đổi danh sách lựa chọn thành 3 tùy chọn:「指定せずに検索」「配送担当者で検索」「端末見積書番号から検索」 | c-734908900 | | | | | Bỏ tùy chọn cũ, thêm「配送担当者で検索」|
| 2 | Screen Flow & Luồng Xử lý | Tạo thiết kế màn hình chọn配送担当者: hiển thị button「自店配送」và「協力店検索」 | c-734908900 | | | | | |
| 3 | Screen Flow & Luồng Xử lý | Tạo thiết kế màn hình chọn担当者 sau khi chọn協力店 (có button「担当者検索」) | c-734908900 | | | | | |
| 4 | Hiển thị & Đồng bộ Thông tin | Khi chọn「自店配送」: hiển thị thông tin cửa hàng của mình tại vùng tương ứng | c-734912154 | | | | | |
| 5 | Cấu trúc Layout & Vị trí Thông tin | Đổi nền trắng để hiển thị màn hình lựa chọn (không hiện trên nền màn担当者) | c-734964609 | | | | | Tham chiếu POS_UI-180 |
| 6 | Hiển thị & Đồng bộ Thông tin | Xóa guide message「～を選択してください」(từ「検索方法」lặp lại quá nhiều) | c-734964609 | | | | | |
| 7 | Hiển thị & Đồng bộ Thông tin | Sửa text vùng nền xanh thành「検索方法選択」(giữ viền xanh, xóa「検索方法」riêng lẻ) | c-734964609 | | | | | |
| 8 | Hiển thị & Đồng bộ Thông tin | Đổi text「指定なし」thành「指定せずに検索」 | c-734964609 | | | | | |
| 9 | UI Components & Controls | Điều chỉnh kích thước button「閉じる」nhỏ hơn để phân biệt với 3 button lựa chọn | c-734964609 | | | | | |

---

## [POS_UI-157] C000111_未承認一覧表示
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | UI Components & Controls | Đổi header cột「選択」thành text「選択」(không dùng checkbox control) | c-734851135 | | | | | |
| 2 | Hiển thị & Đồng bộ Thông tin | Sắp xếp cột theo thứ tự và tên hiện hành: No・見積日時・配送端末見積書番号・配送担当者・お客様氏名・数量・金額 | c-734851135 | | | | | Xóa cột「承認者」|
| 3 | UI Components & Controls | Đổi button xanh thành「承認」 | c-734851135 | | | | | |
| 4 | Visual Style | Đổi màu button「詳細」trùng với màu button「印刷」 | c-734851135 | | | | | |
| 5 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh scrollbar không che lên cột金額 | c-734851135 | | | | | Hiện tại khác spec màn売上 |
| 6 | Hiển thị & Đồng bộ Thông tin | Hiển thị dữ liệu mẫu mỗi dòng No khác nhau, tính đến độ dài ký tự tối đa, thêm tooltip | c-734851135 | | | | | Áp dụng cho tất cả màn tương tự |
| 7 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh khoảng trắng trên/dưới để hiển thị gần 18 dòng (như hiện hành 1 trang 18 dòng) | c-734851135 | | | | | |
| 8 | UI Components & Controls | ~~Thêm các function button (trừ端末見積検索)~~ → **Tạm hoãn**, đang xem xét vị trí đặt button | c-736194034 | | | | | Giữ lại để follow-up |

---

## [POS_UI-158] C000114_詳細
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa guide message các tab từ nội dung màn「担当者入力」sang nội dung phù hợp với từng tab | c-734869058 | | | | | |
| 2 | UI Components & Controls | Tab明細: tạo thiết kế thêm/sửa/xóa商品明細 theo màn売上 | c-734869058 | | | | | |
| 3 | UI Components & Controls | Thêm button「対象」「対象外」「承認」vào vùng footer | c-734869058 | | | | | |
| 4 | Input Fields & Form Design | Tab摘要欄: tạo thiết kế với nội dung MAX (1 dòng 45 ký tự toàn giác × 5 dòng) | c-734869058 | | | | | |
| 5 | UI Components & Controls | Tab顧客情報: tạo thiết kế chỉnh sửa thông tin khách theo màn売上 | c-734869058 | | | | | |
| 6 | Hiển thị & Đồng bộ Thông tin | Hiển thị dữ liệu mẫu tính đến độ dài ký tự tối đa | c-734869058 | | | | | |
| 7 | Hiển thị & Đồng bộ Thông tin | Thêm thiết kế thông báo「あんしんパスポート会員ではない」khi khách hàng không phải hội viên | c-734944783 | | | | | |

---

## [POS_UI-160] C000115_別紙内容確認
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Tab & Thông tin Chi tiết / Consistency | Đổi thiết kế màn hình thành dạng hiển thị tab từ「次回訪問予定」đến「コメント」(giống C000114_詳細) | c-734882594 | | | | | |
| 2 | Screen Flow & Luồng Xử lý | Khi mở màn hình, focus vào tab「次回訪問予定」 | c-734882594 | | | | | Theo chuẩn hiện hành |
| 3 | Tab & Thông tin Chi tiết / Consistency | Thêm tab「次回訪問予定」～「コメント」vào màn C000114_詳細 theo ảnh đính kèm | c-736195478 | | | | | Làm rõ comment 734882594 |

---

## [POS_UI-161] C000116_次回訪問予定
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734888361 | | | | | Áp dụng cho các màn tương tự |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Căn phải số枠数 | c-734888361 | | | | | |
| 3 | Tab & Thông tin Chi tiết / Consistency | Thêm tab「次回訪問予定」～「コメント」vào màn C000114_詳細 | c-736196091 | | | | | Tham chiếu POS_UI-160#736195478 |

---

## [POS_UI-162] C000117_見積内容
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734913270 | | | | | |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Tách thành 2 vùng: vùng nhập liệu + vùng hiển thị danh sách đã nhập (như app hiện hành) | c-736182674 | | | | | |
| 3 | UI Components & Controls | Chỉ hiển thị button ゴミ箱・鉛筆・↑↓ khi touch vào dòng trong vùng hiển thị | c-736182674 | | | | | |
| 4 | Screen Flow & Luồng Xử lý | Chỉnh sửa dòng đã có: chỉ khi touch button 鉛筆 → nội dung dòng đó hiện lên vùng nhập liệu | c-736182674 | | | | | |
| 5 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng khác nhau, tính đến độ dài ký tự tối đa | c-736182674 | | | | | |
| 6 | Hiển thị & Đồng bộ Thông tin | Cột No hỗ trợ tối đa 99 dòng | c-736182674 | | | | | |
| 7 | Screen Flow & Luồng Xử lý | Áp dụng cùng thiết kế cho các màn tương tự (売上返品・内容変更, 配送情報変更...) | c-736182674 | | | | | |
| 8 | Tab & Thông tin Chi tiết / Consistency | Thêm tab「次回訪問予定」～「コメント」vào màn C000114_詳細 | c-736196147 | | | | | Tham chiếu POS_UI-160#736195478 |

---

## [POS_UI-163] C000118_見積結果
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Screen Flow & Luồng Xử lý | Khi di chuyển mục sang「選択済み」, vẫn giữ mục đó ở danh sách bên trái | c-734915564 | | | | | VD: chuyển「00003」vẫn còn trong見積結果 |
| 2 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734915564 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng khác nhau, tính đến độ dài ký tự tối đa | c-734915564 | | | | | |
| 4 | Tab & Thông tin Chi tiết / Consistency | Thêm tab「次回訪問予定」～「コメント」vào màn C000114_詳細 | c-736196224 | | | | | Tham chiếu POS_UI-160#736195478 |

---

## [POS_UI-165] C000120_店舗への連絡
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Screen Flow & Luồng Xử lý | Khi di chuyển mục sang「選択済み」, vẫn giữ mục đó ở danh sách bên trái | c-734922041 | | | | | |
| 2 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734922041 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng khác nhau, tính đến độ dài ký tự tối đa | c-734922041 | | | | | |
| 4 | Tab & Thông tin Chi tiết / Consistency | Thêm tab「次回訪問予定」～「コメント」vào màn C000114_詳細 | c-736196443 | | | | | Tham chiếu POS_UI-160#736195478 |

---

## [POS_UI-166] C000121_コメント
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 ～ 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh khoảng trắng trên/dưới để hiển thị được 12 dòng mà không cần scroll (hiện hành 12 dòng) | c-734924654 | | | | | |
| 2 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734924654 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng khác nhau, tính đến độ dài ký tự tối đa | c-734924654 | | | | | |
| 4 | Tab & Thông tin Chi tiết / Consistency | Thêm tab「次回訪問予定」～「コメント」vào màn C000114_詳細 | c-736196516 | | | | | Tham chiếu POS_UI-160#736195478 |

---

## [POS_UI-167] C000185_明細入力
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | UI Components & Controls | Đổi thiết kế明細 từ dạng bảng sang dạng card (như màn売上) | c-735253333 | | | | | |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh để hiển thị 3 dòng明細 (1 giao dịch tối đa 3 dòng) | c-735253333 | | | | | |
| 3 | UI Components & Controls | Thêm thiết kế tooltip vào vùng hiển thị明細 | c-735253333 | | | | | Áp dụng cho các màn tương tự |
| 4 | UI Components & Controls | Thêm button tìm kiếm theo型番 hoặc phương án khác | c-735253333 | | | | | |
| 5 | UI Components & Controls | Đổi text button「取消」thành「在庫予約を取消」và chuyển sang vị trí bên trái | c-735253333 | | | | | |
| 6 | Hiển thị & Đồng bộ Thông tin | Tạo thiết kế trường hợp không có在庫 (No1 hiển thị trạng thái hết hàng) và đính kèm vào ticket | c-735253333 | | | | | |
| 7 | UI Components & Controls | Thêm button camera vào ô nhập在庫予約番号 (hỗ trợ quét barcode) | c-735253333 | | | | | |
| 8 | Input Fields & Form Design | Tạo thiết kế hiển thị keyboard khi nhập tay在庫予約番号 | c-735253333 | | | | | |
| 9 | Input Fields & Form Design | Điều chỉnh tỷ lệ kích thước textbox và button (button hiện tại quá lớn, trông như UI chọn) | c-735253333 | | | | | |
| 10 | Hiển thị & Đồng bộ Thông tin | Xóa title hoặc label「在庫予約番号」(hai nơi hiển thị text giống nhau) | c-735253333 | | | | | |
| 11 | UI Components & Controls | Thiết kế màn取消: dùng dạng card (không có明細 nên giống màn配送情報変更) | c-735253333 | | | | | |
| 12 | Hiển thị & Đồng bộ Thông tin | Đổi text button「進む」thành「取消」 | c-735253333 | | | | | |
| 13 | Hiển thị & Đồng bộ Thông tin | Thêm hiển thị数量 vào màn取消 | c-735253333 | | | | | Tham chiếu ảnh pasted-2026.05.12-17.14.38 |

---

## [POS_UI-169] C000186_在庫引当確認 / 予約取消確認
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Visual Style | Tăng font size câu「DC在庫の引当を行いますか。」cho to và nổi bật hơn | c-735179276 | | | | | |
| 2 | Hiển thị & Đồng bộ Thông tin | Xóa tiêu đề (title) vì trùng nội dung với body | c-735179276 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Sửa body thành「DC在庫の引当を行いますか。」 | c-735179276 | | | | | Thêm chữ の: 在庫引当 → 在庫**の**引当 |
| 4 | UI Components & Controls | Đổi 2 nút lựa chọn thành「いいえ」「はい」 | c-735179276 | | | | | Thứ tự: いいえ trước, はい sau |

---

## [POS_UI-171] C000176_空き状況一覧表示
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-14 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Vùng「センター店」chỉ hiển thị tên cửa hàng (không lặp mã); tối đa toàn giác 16 ký tự | c-736333111 | | | | | Mã011-9112 đã hiện ở cột bên trái |
| 2 | UI Components & Controls | Cập nhật thiết kế nút前週/今週/翌週 (前週 không bấm được khi đang ở tuần hiện tại; 翌週 cho phép xem hơn 1 năm) | c-736333111 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Sửa typo「アリア」thành「エリア」 | c-736333111 | | | | | |
| 4 | Hiển thị & Đồng bộ Thông tin | Hiển thị枠数 dạng 3 chữ số (tối đa 999) | c-736333111 | | | | | |
| 5 | UI Components & Controls | Thêm button「予約処理」 | c-736333111 | | | | | |
| 6 | Screen Flow & Luồng Xử lý | Làm rõ luồng: chọn エリア + 日付 → bấm「予約処理」→ chuyển màn予約 | c-736333111 | | | | | Hiện tại khó biết エリア/日付 có thể bấm được |
| 7 | Screen Flow & Luồng Xử lý | Tạo thiết kế: bấm Web受注 → chuyển sang màn nhập Web受注番号 | c-736333111 | | | | | |
| 8 | Hiển thị & Đồng bộ Thông tin | Tạo 2 phiên bản: có hiển thị / không hiển thị button Web受注 (Web通販店 → hiện, không phải → ẩn) | c-736333111 | | | | | |
| 9 | Cấu trúc Layout & Vị trí Thông tin | Chuyển button「取消」sang bên trái (bên phải button「戻る」) | c-736333111 | | | | | |

---

## [POS_UI-173] C000178_配送工事区分選択
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | UI Components & Controls | Đồng bộ thiết kế button 時間帯 theo màn配送情報変更_時間帯選択 | c-735764136 | | | | | |
| 2 | Input Fields & Form Design | Tạo thiết kế hiển thị keyboard khi nhập số工事重み | c-735764136 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Tạo thiết kế trường hợp時間帯 = 0件 (hiển thị 0/10, button không thể bấm/非活性) | c-735764136 | | | | | Áp dụng cho các màn tương tự |
| 4 | Hiển thị & Đồng bộ Thông tin | Sửa guide message từ nội dung予約担当者入力 sang nội dung phù hợp với màn hình này | c-735764136 | | | | | |
| 5 | Hiển thị & Đồng bộ Thông tin | Sửa label「エリア」thành tên エリア thực (vd 水戸, いわき) thay vì mã cửa hàng | c-735764136 | | | | | |
| 6 | Hiển thị & Đồng bộ Thông tin | Thêm vùng hiển thị comment エリア (toàn giác 50 ký tự × 2 dòng) | c-735764136 | | | | | |

---

## [POS_UI-174] C000180_指定方法選択
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Xóa guide「～を選択してください」(chữ「指定方法」lặp lại 2 lần, bỏ guide bớt) | c-735781686 | | | | | |
| 2 | Hiển thị & Đồng bộ Thông tin | Xóa text「検索方法」trên nền xanh | c-735781686 | | | | | |
| 3 | UI Components & Controls | Điều chỉnh kích thước button「閉じる」nhỏ hơn để phân biệt với button lựa chọn | c-735781686 | | | | | |

---

## [POS_UI-175] B0401_エリア絞込
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Cấu trúc Layout & Vị trí Thông tin | Căn giữa cột エリアコード | c-735779167 | | | | | |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh độ rộng cột エリア名称 đủ chứa tối đa toàn giác 30 ký tự; điều chỉnh kích thước subform tương ứng | c-735779167 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng No khác nhau | c-735779167 | | | | | |
| 4 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh scrollbar không che lên明細 | c-735779167 | | | | | |
| 5 | UI Components & Controls | Đổi text button「進む」thành「確定」 | c-735779167 | | | | | |
| 6 | UI Components & Controls | Xóa button「特定エリア表示」(chức năng hiện không sử dụng) | c-735779167 | | | | | |

---

## [POS_UI-178] C000182_店舗情報入力
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-13 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Input Fields & Form Design | Xác nhận và thiết kế nội dung hiển thị sau search (法人コード+法人名 / 店舗コード+店舗名); tạo cả trạng thái chưa nhập và đã nhập | c-736225727 | | | | | |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Căn giữa JISコード và 配送頻度 | c-736225727 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Sửa typo「頻度」(「頻」bị viết sai) | c-736225727 | | | | | |
| 4 | Hiển thị & Đồng bộ Thông tin | Sửa dữ liệu mẫu địa chỉ từ「ミトミツクニ」sang dạng「都道府県 + 市」 | c-736225727 | | | | | |
| 5 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng明細 khác nhau | c-736225727 | | | | | |
| 6 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh scrollbar không che lên明細 | c-736225727 | | | | | |
| 7 | UI Components & Controls | Xóa button「確定」 | c-736225727 | | | | | |
| 8 | UI Components & Controls | Đổi màu button「印刷」sang màu xanh | c-736225727 | | | | | |
| 9 | Screen Flow & Luồng Xử lý | Tạo thiết kế màn hình sau khi bấm button「宅配不可エリア」 | c-736225727 | | | | | |

---

## [POS_UI-180] C000123_検索方法選択
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734964609 | | | | | |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Đổi nền trắng để hiển thị màn hình lựa chọn (không hiện trên nền màn担当者) | c-734964609 | | | | | |
| 3 | Hiển thị & Đồng bộ Thông tin | Xóa guide「～を選択してください」; sửa text vùng nền xanh thành「検索方法選択」 | c-734964609 | | | | | |
| 4 | Hiển thị & Đồng bộ Thông tin | Đổi text「指定なし」thành「指定せずに検索」 | c-734964609 | | | | | |
| 5 | UI Components & Controls | Điều chỉnh kích thước button「閉じる」nhỏ hơn (tránh nhầm 3 lựa chọn) | c-734964609 | | | | | |

---

## [POS_UI-181] C000125_端末見積書検索サブフォーム
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734954088 | | | | | |
| 2 | Tab & Thông tin Chi tiết / Consistency | Áp dụng cùng sửa đổi với POS_UI-156#comment-732589585 (xem comment gốc trên Backlog) | c-734954088 | | | | | Cần xem comment POS_UI-156 để biết chi tiết |

---

## [POS_UI-182] C000124_未承認一覧表示
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734953344 | | | | | |
| 2 | UI Components & Controls | Đổi header cột「選択」thành text「選択」(không dùng checkbox control) | c-734953344 | | | | | |
| 3 | UI Components & Controls | Thêm function button (ngoài端末見積検索) hoặc phương án khác để thực hiện chức năng | c-734953344 | | | | | |
| 4 | UI Components & Controls | Đổi button xanh thành「印刷」 | c-734953344 | | | | | |
| 5 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh scrollbar không che lên cột金額 | c-734953344 | | | | | |
| 6 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng No khác nhau + thêm tooltip | c-734953344 | | | | | Áp dụng cho các màn tương tự |
| 7 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh khoảng trắng trên/dưới để hiển thị gần 18 dòng | c-734953344 | | | | | |

---

## [POS_UI-183] C000127_詳細
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734936232 | | | | | |
| 2 | Tab & Thông tin Chi tiết / Consistency | Tab明細: đổi sang thiết kế giống màn売上 (tham chiếu配送情報変更) | c-734936232 | | | | | Không cần tính năng edit明細 |
| 3 | Input Fields & Form Design | Tab摘要欄: áp dụng cùng sửa đổi với POS_UI-151 (1 dòng 45 ký tự × 5 dòng MAX) | c-734936232 | | | | | |
| 4 | Tab & Thông tin Chi tiết / Consistency | Tab顧客情報: thêm thông tin hiển thị tham chiếu màn顧客 trong売上返品・売上内容変更 | c-734936232 | | | | | |
| 5 | Hiển thị & Đồng bộ Thông tin | Thêm thiết kế thông báo「あんしんパスポート会員ではない」khi khách hàng không phải hội viên | c-734945894 | | | | | |

---

## [POS_UI-184] C000126_印刷確認
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Đổi text「お客様控えのみ」thành「お客様控えのみを印刷」 | c-734983226 | | | | | Thêm「を印刷」|
| 2 | Hiển thị & Đồng bộ Thông tin | Đổi text「会員番号記載」thành「見積書に会員番号を記載」 | c-734983226 | | | | | Thêm「見積書に～を記載」|

---

## [POS_UI-185] C000128_別紙内容確認
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734927112 | | | | | |
| 2 | Tab & Thông tin Chi tiết / Consistency | Đổi thiết kế hiển thị tab từ「次回訪問予定」đến「コメント」(giống C000114_詳細) | c-734927112 | | | | | Tham chiếu POS_UI-160#734882594 |
| 3 | Screen Flow & Luồng Xử lý | Khi mở màn hình, focus vào tab「次回訪問予定」 | c-734927112 | | | | | |

---

## [POS_UI-186] C000129_次回訪問予定
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734927913 | | | | | |
| 2 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734927913 | | | | | Tham chiếu POS_UI-161#734888361 |
| 3 | Cấu trúc Layout & Vị trí Thông tin | Căn phải số枠数 | c-734927913 | | | | | |

---

## [POS_UI-187] C000130_見積内容
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734927342 | | | | | |
| 2 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734927342 | | | | | Tham chiếu POS_UI-162#734913270 |

---

## [POS_UI-188] C000131_見積結果
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734926686 | | | | | |
| 2 | Screen Flow & Luồng Xử lý | Khi di chuyển mục sang「選択済み」, vẫn giữ mục ở danh sách bên trái | c-734926686 | | | | | Tham chiếu POS_UI-163#734915564 |
| 3 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734926686 | | | | | |
| 4 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng khác nhau, tính đến độ dài ký tự tối đa | c-734926686 | | | | | |

---

## [POS_UI-190] C000133_店舗への連絡
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734926004 | | | | | |
| 2 | Tab & Thông tin Chi tiết / Consistency | Áp dụng cùng sửa đổi với POS_UI-164#comment-734921550 (xem comment gốc trên Backlog) | c-734926004 | | | | | Cần xem comment POS_UI-164 để biết chi tiết |

---

## [POS_UI-191] C000134_コメント
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Sửa tiêu đề màn hình thành「見積書未印刷一覧（配送端末）」 | c-734926251 | | | | | |
| 2 | Cấu trúc Layout & Vị trí Thông tin | Điều chỉnh khoảng trắng trên/dưới để hiển thị được 12 dòng mà không cần scroll | c-734926251 | | | | | Tham chiếu POS_UI-166#734924654 |
| 3 | Visual Style | Đồng bộ thiết kế trường見積数量・金額 theo các màn hình khác | c-734926251 | | | | | |
| 4 | Hiển thị & Đồng bộ Thông tin | Dữ liệu mẫu mỗi dòng khác nhau, tính đến độ dài ký tự tối đa | c-734926251 | | | | | |

---

## [POS_UI-194] 返品エラー通知
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Xóa tiêu đề「通知」(không cần thiết) | c-735365601 | | | | | |
| 2 | UI Components & Controls | Thu nhỏ button「終了」về cùng kích thước với các button khác | c-735365601 | | | | | |

---

## [POS_UI-195] 元伝と新黒決済確認
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Cập nhật thiết kế mới nhất: thêm hiển thị「お買上げ総数」và「総額」(vùng khung đỏ trong ảnh) | c-735380732 | | | | | |
| 2 | Hiển thị & Đồng bộ Thông tin | Thêm hiển thị「未決済金額」vào thiết kế (vùng khung xanh trong ảnh) | c-735380732 | | | | | |

---

## [POS_UI-196] C000058_決済種別変更の確認
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Xóa tiêu đề「決済種別変更」ở trên cùng | c-735321651 | | | | | |

---

## [POS_UI-197] 元伝カード決済引き継ぎの確認
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Xóa tiêu đề「元伝カード決済」ở trên cùng | c-735320137 | | | | | |

---

## [POS_UI-198] 元伝決済時カード持ち確認
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | Xóa tiêu đề「元伝決済時カード」ở trên cùng | c-735312896 | | | | | |
| 2 | Screen Flow & Luồng Xử lý | Xác nhận luồng sau khi chọn「元伝決済時カード」: tự động chuyển màn hay cần thêm button「確定」? Bổ sung thiết kế tương ứng | c-735312896 | | | | | Hiện tại không có button xác nhận |

---

## [POS_UI-201] C000047_客先配送予定日
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-12 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | UI Components & Controls | Đồng bộ thiết kế theo màn配送情報変更_時間帯選択 (tham chiếu ảnh đính kèm) | c-734947119 | | | | | |

---

## [POS_UI-203] C000183_空き状況一覧表示
- Người phụ trách: VTI アイン
- Status: 30_差戻／修正依頼
- Ngày comment: 2026-05-08 (SMJ 河野)

| # | Nhóm | Việc cần sửa | 出典 | Round 1 | Round 2 | Round 3 | M | Remark |
|---|------|-------------|------|---------|---------|---------|---|--------|
| 1 | Hiển thị & Đồng bộ Thông tin | ⚠️ **Xác nhận với SMJ 河野**: ticket này có thể trùng với POS_UI-171 (thiếu hiển thị センター店名). Nếu là ticket trùng → đề xuất đóng ticket này | c-733352481 | | | | | Đợi phản hồi trước khi sửa |
