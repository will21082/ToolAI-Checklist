# SHARP POS UI/UX — Checklist Screen Design

| Mục | Giá trị |
|---|---|
| VTI Document Code | 09-CL/PM/VTI |
| VTI Document Version | 1.0 |
| Effective Date | 2019/02/22 |

---

## Record of Change

| No | Date | Version | PIC | Change Description | Reviewer | Approver |
|---|---|---|---|---|---|---|
| 1.0 | 2026/03/06 | 1.0 | Nguyen Dinh Hiep | Create New | | |

---

## Checklist từ Feedback của khách

| # | Phân loại | Item | Rule | Round 1 | Round 2 | Round 3 | Mandatory | Remark | Guideline |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Header | Tên màn hình | Hiển thị tên menu tương ứng | | | | | | Update correct company name as VTI, correct author, correct document name, correct title |
| 2 | | Màu header | Màn thông thường: màu 00838C (xanh) / Màn hủy: màu D43E3E (đỏ) | | | | | | |
| 3 | | Thông tin nhân viên, hội viên (tên, mã,...) | Để màu 00838C (xanh), dạng textlink (có gạch chân) | | | | | | With English Document: use spell check of MS Office |
| 4 | Footer | Stepbar | Nút back luôn ở bên trái, các button chức năng sắp xếp từ phải qua trái, thanh step bar luôn hiển thị đủ tối đa 5 step | | | | | | |
| 5 | Visual Style | Tab | Tab kiểu Windows, bo tròn | | | | | | Update hyperlink in table of content to correct destination |
| 6 | Component Behavior | List data | Hiển thị số lượng kết quả data search / data nhập ở phía trên list | | | | | | |
| 7 | | Table | Có ký hiệu sort ở các cột (trừ cột No) trong bảng | | | | | | |
| 8 | | Popup | Button đóng popup là 閉じる, đặt ở góc trái phía dưới, không dùng button X | | | | | | |
| 9 | Data Format | Số tiền | Số tiền âm để là ¥-XXX | | | | | | |
| 10 | | Text Alignment | Data dạng code thì căn giữa, dạng character thì căn trái, dạng tiền tệ thì căn phải | | | | | | Đồng bộ Component Diagram và Structure Diagram, đảm bảo mọi design trong Component Diagram triển khai đúng trên Structure Diagram |
| 11 | Layout & Size | Field | Field số tiền để size to để dễ focus, textbox không để quá dài | | | | | | |
| 12 | | Popup | Phần popup để size to để dễ thao tác, không để phần ngoài popup thừa nhiều | | | | | | |

---

## Checklist từ File Guide Design của khách

| # | Check item | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|
| **1** | **Screen Layout & Responsive Design** | | | | | |
| 1.1 | Mọi màn hình có đủ 3 vùng bắt buộc: Header Area / Content Area / Footer Area không? | | | | | |
| 1.2 | Header Area có chứa đầy đủ: tên menu, guide message, thông tin cửa hàng, hamburger menu không? | | | | | |
| 1.3 | Footer Area có chứa nút điều hướng chính ("Quay lại", "Tiến tới") và progress flow không? | | | | | |
| 1.4 | Tất cả vùng chính (Header/Content/Footer) có chiếm 100% chiều rộng vùng hiển thị thiết bị không? | | | | | |
| 1.5 | Chiều cao Content Area có được tính tự động = Chiều cao màn hình − Header − Footer không? | | | | | |
| 1.6 | Layout nội bộ bên trong Content Area có dùng tỷ lệ % thay vì giá trị tuyệt đối (px) không? | | | | | |
| 1.7 | Font weight Medium có được dùng cho danh sách, giá trị nhập/chọn không? | | | | | |
| 1.8 | Kích thước font có được điều chỉnh linh hoạt theo từng mức độ phân giải (stage-switching) không? | | | | | |
| 1.9 | Thiết kế có chỉ dùng màu trong bảng màu đã định nghĩa trong guideline, không tự ý thêm màu mới không? | | | | | |
| **2** | **Touch & Mouse Support** | | | | | |
| 2.1 | Thiết kế có hỗ trợ cả thao tác cảm ứng (tablet) và chuột (Windows Desktop) không? | | | | | |
| 2.2 | Touch target size có tuân thủ nguyên tắc Touch UI tiêu chuẩn (kích thước vùng chạm đủ lớn) không? | | | | | |
| **3** | **Scroll Operation** | | | | | |
| 3.1 | Desktop: có hiển thị scrollbar; Tablet: KHÔNG hiển thị scrollbar mà dùng swipe không? | | | | | |
| 3.2 | Scrollbar chỉ xuất hiện khi nội dung cần scroll (không hiển thị mặc định) không? | | | | | |
| 3.3 | Scroll chỉ theo chiều dọc (vertical only), không scroll ngang không? | | | | | |
| 3.4 | Khi nhấn giữ scrollbar có zoom up vùng scroll để dễ điều hướng chính xác không? | | | | | |
| **4** | **UI Controls — Tuân thủ Spec Chuẩn** | | | | | |
| 4.1 | Hamburger Menu, Notification Badge, Breadcrumb, Pagination có được dùng đúng spec control đã chuẩn hóa trong guideline không? | | | | | |
| 4.2 | Text Box, Dropdown List, Calendar, Label có được dùng đúng spec control đã chuẩn hóa không? | | | | | |
| 4.3 | List/Table, Tooltip, Popup Message, Guide Message có được dùng đúng spec control đã chuẩn hóa không? | | | | | |
| 4.4 | Không tự ý tạo component mới ngoài danh sách control đã được approve không? | | | | | |
| **5** | **Accessibility & Quy trình Thay đổi** | | | | | |
| 5.1 | Thiết kế có tuân thủ tiêu chuẩn accessibility cho cả Desktop và Tablet không? | | | | | |
| 5.2 | Mọi ngoại lệ (exception) so với guideline có ghi rõ lý do và được stakeholder đồng thuận trước khi áp dụng không? | | | | | |
| 5.3 | Khi guideline conflict với usability thực tế, có ưu tiên trải nghiệm người dùng (usability) hơn không? | | | | | |
| 5.4 | Mọi thay đổi thiết kế có tuân theo quy trình: Đề xuất → Thảo luận → Đồng ý khách hàng → Cập nhật guideline → Version management không? | | | | | |

---

## Checklist Template (Screen Design Review)

Thông tin review: Project name / Project manager / Products-Files / Reviewer / Review date (yyyy/mm/dd)

| # | Check Item | Mandatory | Remark / Guideline |
|---|---|---|---|
| **0** | **Format** | | |
| 0.1 | Is Properties (signature, company name) updated correctly? | | Update correct company name as VTI, correct author, document name, title |
| 0.2 | Is document updated following VTI's template? | M | |
| 0.3 | Have you checked grammar/spelling? If translated, checked against origin document? | | With English Document: use MS Office spell check |
| 0.4 | Have you explained for diagram in document? | | Update note to explain each component and relationship in Component/Structure Diagram |
| 0.5 | Have you updated sheet [History]? | | Update what changed each version |
| 0.6 | Have you updated sheet [Table of Content]? | | Update hyperlink to correct destination |
| 0.7 | Have you checked all link/Url in document? | | No breaking/error link |
| **1** | **Screen** | | |
| 1.1 | Have you listed up all screens needed to be implemented? | M | |
| 1.2 | Have you listed up all items needed to be implemented on screen? | M | |
| 1.3 | Listed item for each screen is detailed enough to implement? | | Divide screen into basic items: label, button, image,… |
| 1.4 | Have you described detail enough to implement for each item in screen? | | |
| 1.5 | For each item, classified (static/dynamic), filled all information? | M | |
| 1.6 | Can you make sure information for each item is correct with requirement? | | |
| **2** | **Language** | | |
| 2.1 | Have you designed language management for text components? | M | |
| 2.2 | Have you filled content for each language of each component? | | e.g. 20 components × 3 languages = 60 entries |
| 2.3 | Is text content really clear, concise and meaningful? | M | |
| 2.4 | Are all words spelled correctly, abbreviations only when space is limited? | | |
| **3** | **Component** | | |
| 3.1 | Is design size for button/image/select area good and easy to interact (esp. touch)? | M | Synchronize Component Diagram & Structure Diagram |
| 3.2 | Visual consistent: typeface/button/text/color unified across system? | M | List components by group/layer, describe functions in Structure Diagram |
| 3.3 | Text alignment suitable for each language/market? | | e.g. English left, Arabic right |
| **4** | **Layout** | | |
| 4.1 | Have you designed screen for all resolutions? | M | |
| 4.2 | Have you designed screen for all monitor sizes (10", 11",…)? | | |
| 4.3 | Have you prepared image/font/layout for all components in many resolutions? | M | |
| 4.4 | Is design for text (font size/family/color contrast) comfortable? | M | e.g. font <16px hard to support multi-size |
| **5** | **General** | | |
| 5.1 | Meaningful, concise messages when error/problem exists? | M | |
| 5.2 | Error messages include guidance for correct entry? | M | |
| 5.3 | Is screen well organized and easy to use? | M | |
| 5.4 | Is screen well composed? | | |
| 5.5 | Is related information grouped together? | | |
| 5.6 | Multi-screen for one logical data: related info located together? | M | |
| 5.7 | Most important fields located where easy to see? | M | |
| 5.8 | Information presented in order the user needs? | | |
| 5.9 | Optional/mandatory fields marked clearly? | | |
| 5.10 | Default values provided where appropriate? | | |
| 5.11 | Field sizes large enough for all valid entries? | | |
| 5.12 | Design follows UI standard (Apple HIG / Google Material)? | | |
| **6** | **Screen Flow** | | |
| 6.1 | Have you described all screen flows? | M | Purpose of flow + Screen Flow Diagram |
| 6.2 | Each flow described completely? | M | Draw full event & related screen, note main action |
| 6.3 | Described condition to start/end each flow? | M | |
| 6.4 | Described condition to switch flow? | M | |
| **7** | **Screen Transition** | | |
| 7.1 | Every screen in design doc listed in transition document? | M | |
| 7.2 | Drawn all transitions between screens? | M | |
| 7.3 | Described all conditions to do screen transition? | M | |
| 7.4 | Listed all exceptions preventing transition? | M | |
| 7.5 | Described conditions to show sub screen & its content? | M | |

Summary: Number of OK / NOK / N/A items (per Round). Review Result: Pass / Review Again / Acceptable.

---

## Comment-Design (Dữ liệu comment thực tế)

Thống kê: Internal Comment 7 (Resolved 3, Closed 4) — External Comment 32 (In-Progress 1, Resolved 31).

| STT | Date | Author | Assignee | Flow | Screen | Nội dung | Status |
|---|---|---|---|---|---|---|---|
| 1 | 2026-01-15 | ngoc.phamvan | ninh.nguyenhai1 | 売上返品・売上内容変更 | Z0001 担当者入力 | Chưa nhập nên phải để trống hoặc gạch ngang | Resolved |
| 2 | 2026-01-15 | anh.nguyenthi | an.tranhai | 売上返品・売上内容変更 | A0407 顧客入力 | Sửa text button | Resolved |
| 3 | 2026-01-19 | anh.nguyenthi | an.tranhai | 売上速報 | C0001 照会メニュー | Sửa thành text 売上速報 | Resolved |
| 5 | 2026-02-14 | Customer | an.tranhai | 売上速報 | C0701 一覧表示 | Vui lòng bổ sung hiển thị số lượng (góc trên bên phải) | Resolved |
| 6 | 2026-02-14 | Customer | an.tranhai | 売上速報 | C0701 一覧表示 | Phần header vui lòng hiển thị tên menu thay vì tên màn hình | Resolved |
| 7 | 2026-02-14 | Customer | an.tranhai | 売上速報 | C0701 一覧表示 | Vui lòng thêm ký hiệu sắp xếp vào các cột ngoài cột No | Resolved |
| 8 | 2026-02-14 | Customer | an.tranhai | 売上速報 | C0701 一覧表示 | Bo tròn ở thiết kế tab | Resolved |
| 9 | 2026-02-14 | Customer | ninh.nguyenhai1 | 売上返品・売上内容変更 | Z001, A0401, A0402 | Vui lòng hiển thị thanh tiến trình ở phần footer | Resolved |
| 10 | 2026-02-14 | Customer | ninh.nguyenhai1 | 売上返品・売上内容変更 | A0405, A0403 | Luồng tiến trình tiếp tục theo thứ tự: 担当者 > 伝票番号 > 返品種別, thay đổi tùy kết quả "返品のみ" hoặc "再売上あり" | Resolved |
| 11 | 2026-02-14 | Customer | ninh.nguyenhai1 | 売上返品・売上内容変更 | A0405 | Phần header hiển thị tên menu thay vì tên màn hình | Resolved |
| 12 | 2026-02-14 | Customer | ninh.nguyenhai1 | 売上返品・売上内容変更 | A0405 | Có thể thể hiện cách nào đó để người dùng biết đã chọn "返品なし" không? | Resolved |
| 13 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0201 | Pattern nhập liệu dùng radio chọn 1 trong 2: (1) Cửa hàng bán & Số phiếu bán (2) Chỉ số đơn hàng Web; chỉ cho nhập mục tương ứng pattern đã chọn | Resolved |
| 14 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0102 | Về thiết kế tab, bo tròn giống tab Windows | Resolved |
| 15 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | Tất cả màn trong luồng | Hiển thị cửa hàng bán và số phiếu bán trên toàn bộ màn hình của luồng | Resolved |
| 16 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0102 | Hiển thị phân loại xuất kho, cửa hàng giao, tổng tiền, ngày dự kiến giống hiện hành | Resolved |
| 17 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0102 | Đặt "Thông tin địa chỉ giao hàng khác" bên cạnh "Thông tin người mua" | Resolved |
| 18 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0102 | Tab thông tin sản phẩm: hiển thị số lượng (mọi màn), mục chi tiết giữ như hiện hành | Resolved |
| 19 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0102 | Tab thanh toán: hiển thị số lượng mua, tổng tiền, số tiền còn lại; bỏ ký tự "-" trước "yên" | Resolved |
| 20 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0102 | Thêm tag "引取商品有り" để nhận biết phiếu nhận hàng | Resolved |
| 21 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0102 tab配送情報 | Cho xác nhận thông tin giao hàng/thi công/khách hàng + môi trường lắp đặt; bỏ mục phân loại đã có ở header; dùng collapse/expand | Resolved |
| 22 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0103 | Loại bỏ thông tin trùng với header | Resolved |
| 23 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0103 | Thể hiện khi có thay đổi ngày dự kiến giao hàng (tick check xanh) | Resolved |
| 24 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | Luồng xuất hóa đơn (figma) | Thiết kế cả luồng đến khi xuất hóa đơn thay đổi thông tin giao hàng | Resolved |
| 25 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0103 | UI dạng công tắc bật/tắt để chuyển đổi xuất / không xuất phiếu đính kèm | Resolved |
| 26 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0118 | Thông tin người mua: bỏ mã JIS, đưa mã KH và số hội viên lên trên | Resolved |
| 27 | 2026-02-15 | Customer | ninh.nguyenhai1 | 配送情報変更 | B0102 | Thông tin địa chỉ giao hàng khác: hiển thị cùng nội dung với người mua (mã KH, số hội viên,…) | Resolved |
| 28 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0201 売上伝票番号入力 | Chuyển 2 mode "Chế độ thường" / "Chế độ hủy" dạng công tắc, mỗi mode hiển thị option qua radio button | Resolved |
| 29 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0202 処理区分選択 | Sửa thiết kế tab theo dạng tab Windows | Resolved |
| 30 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0202 処理区分選択 | Thông tin khách nhận hàng đồng bộ với thông tin người mua thay cho "--" | Resolved |
| 31 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0203 管理票/伝票番号選択 | Giữ thứ tự nhập như hiện tại; header sửa thành cửa hàng hợp tác/mình; button "In" → "Tiếp tục" | In-Progress |
| 32 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0203 管理票/伝票番号選択 | Thêm tag [Thiết bị] khi đọc phiếu phát hành theo hình thức vận hành bằng thiết bị | Resolved |
| 33 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0206 入金額… | Trường hợp thu hộ đến cửa hàng ngày sau: chỉ hiển thị mục nhập số tiền thu, ẩn số vận đơn/số kiện | Resolved |
| 34 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0210 決済 | Bàn phím số phải lớn, hiển thị vị trí cố định như app mock | Resolved |
| 35 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0204 元レシート内容表示 | Hủy hoàn tất: chỉ nhập số tiền thu, bỏ số vận đơn/số kiện | Resolved |
| 36 | 2026-02-16 | Customer | an.tranhai | 入金配送完了 | B0204 → B0209 | Luồng hủy: sau "Tiếp tục" → thanh toán theo số tiền thu đã nhập → màn hình thanh toán | Resolved |
| — | 2026-02-15 | anh.nguyenthi | ninh.nguyenhai1 | 配送情報変更 | | Luồng này đang bị nhầm stepbar của luồng trên | Closed |
| — | 2026-02-16 | anh.nguyenthi | ninh.nguyenhai1 | 入金配送完了 | | Stepbar đang bị nhầm theo luồng trả hàng | Closed |
| — | 2026-02-16 | anh.nguyenthi | ninh.nguyenhai1 | 売上速報 | | Sửa tên màn hình thành tên menu như các luồng trên | Closed |
| — | 2026-02-19 | anh.nguyenthi | an.tranhai | 配送情報変更 | B0102 | Số record sửa lại theo số record trên list | Closed |
| — | 2026-02-19 | anh.nguyenthi | an.tranhai | 配送情報変更 | B0102 | Bảng list thiếu cột 出庫区分 | |

---

## ChecklistDesign — From Comment (Checklist tổng hợp từ comment)

Đây là checklist đã được tổng hợp từ các comment ở sheet Comment-Design.

| # | Check Item | Round 1 | Round 2 | Round 3 | Mandatory | Remark |
|---|---|---|---|---|---|---|
| **1** | **Header & Navigation** | | | | | |
| 0.1 | Tiêu đề màn hình có hiển thị tên menu thay vì tên màn hình (screen name) không? | | | | | |
| 0.2 | Thanh tiến trình (stepbar/progress bar) có hiển thị đúng ở phần footer theo từng luồng không? | | | | | |
| 0.3 | Stepbar có phản ánh đúng luồng đang xử lý (không bị nhầm sang luồng khác) không? | | | | | |
| 0.4 | Thông tin header (cửa hàng bán, số phiếu bán, phân loại xuất kho, tổng tiền, ngày dự kiến,...) có hiển thị đầy đủ và nhất quán trên toàn bộ màn hình trong cùng luồng không? | | | | | |
| **2** | **UI Components & Controls** | | | | | |
| 1.1 | Tab design có được bo tròn theo chuẩn Windows style không? | | | | | |
| 1.2 | Radio button có được dùng đúng cách để chọn một trong nhiều tùy chọn (pattern nhập liệu, chế độ xử lý,...) không? | | | | | |
| 1.3 | Toggle switch (công tắc bật/tắt) có được dùng để thể hiện chuyển đổi trạng thái (xuất/không xuất phiếu, chế độ thường/hủy) không? | | | | | |
| 1.4 | Bàn phím số (numeric keyboard) có đủ lớn và hiển thị ở vị trí cố định trên màn hình thanh toán không? | | | | | |
| 1.5 | Các nút bấm có được đặt tên rõ ràng, phù hợp với hành động ("Tiếp tục" thay vì "In") không? | | | | | |
| 1.6 | Collapse/Expand có được áp dụng để thể hiện thông tin chi tiết có thể thu gọn/mở rộng không? | | | | | |
| **3** | **Hiển thị & Đồng bộ Thông tin** | | | | | |
| 3.1 | Số lượng có hiển thị đầy đủ (góc trên bên phải danh sách, tab thông tin sản phẩm) trên tất cả màn hình liên quan không? | | | | | |
| 3.2 | Thông tin khách hàng (mã KH, số hội viên,...) có đồng bộ nhất quán giữa các màn hình và vùng hiển thị không? | | | | | |
| 3.3 | Trường hợp dữ liệu chưa nhập, có hiển thị trống hoặc dấu gạch ngang (–) không? | | | | | |
| 3.4 | Tag trạng thái đặc biệt ([引取商品有り], [Thiết bị]) có được thêm để nhận biết nhanh loại phiếu/hình thức vận hành không? | | | | | |
| 3.5 | Thông tin trùng lặp với header có được loại bỏ khỏi nội dung màn hình không? | | | | | |
| 3.6 | Khi có thay đổi (ngày dự kiến giao hàng), có indicator trực quan (tick check xanh) không? | | | | | |
| **4** | **Cấu trúc Layout & Vị trí Thông tin** | | | | | |
| 4.1 | Thứ tự các mục nhập liệu có được sắp xếp hợp lý theo luồng thao tác của người dùng không? | | | | | |
| 4.2 | Thông tin địa chỉ giao hàng khác có được đặt cạnh thông tin người mua để dễ đối chiếu không? | | | | | |
| 4.3 | Thông tin quan trọng (mã KH, số hội viên) có được đặt ở vị trí dễ thấy (phía trên) không? | | | | | |
| 4.4 | Các ký hiệu sắp xếp (sort icon) có được thêm vào các cột (ngoại trừ cột No) không? | | | | | |
| 4.5 | Ký tự không cần thiết (dấu "-" trước "yên") có được loại bỏ không? | | | | | |
| **5** | **Screen Flow & Luồng Xử lý** | | | | | |
| 5.1 | Luồng chuyển màn hình có được thiết kế và mô tả đầy đủ đến bước cuối (đến khi xuất hóa đơn) không? | | | | | |
| 5.2 | Mối quan hệ chính-phụ giữa các chức năng (hủy là tùy chọn của hoàn tất) có được thể hiện rõ ràng không? | | | | | |
| 5.3 | Trình tự các bước trong luồng có thể hiện đúng và thay đổi phù hợp theo kết quả lựa chọn không? | | | | | |
| 5.4 | Sau khi nhấn xác nhận/tiếp tục, luồng chuyển màn hình có đúng thiết kế không? | | | | | |
| **6** | **Input Fields & Form Design** | | | | | |
| 6.1 | Pattern nhập liệu có được chuyển đổi bằng radio và chỉ hiển thị mục tương ứng pattern đã chọn không? | | | | | |
| 6.2 | Chế độ thao tác (thường/hủy) có được chuyển đổi bằng toggle và chỉ hiển thị trường phù hợp không? | | | | | |
| 6.3 | Các mục nhập không cần thiết trong từng nghiệp vụ (số vận đơn khi thu hộ đến cửa hàng) có được ẩn không? | | | | | |
| 6.4 | Thứ tự nhập liệu có đúng thiết kế: chọn từ danh sách trước, sau đó nhập số tiền không? | | | | | |
| **7** | **Tab & Thông tin Chi tiết / Consistency** | | | | | |
| 7.1 | Tab thông tin sản phẩm có hiển thị số lượng và giữ nguyên mục chi tiết như hiện hành không? | | | | | |
| 7.2 | Tab thanh toán có hiển thị đầy đủ: số lượng mua, tổng tiền, số tiền còn lại không? | | | | | |
| 7.3 | Tab giao hàng (配送情報) có hiển thị đầy đủ và hỗ trợ collapse/expand không? | | | | | |
| 7.4 | Thông tin phân loại giao hàng/thi công đã có ở header có được loại khỏi tab chi tiết để tránh trùng không? | | | | | |
| 7.6 | Thiết kế (màu, font, button, icon) có nhất quán xuyên suốt các màn hình cùng luồng không? | | | | | |
| 7.7 | Trạng thái đã chọn ("返品なし" đã chọn) có được thể hiện rõ ràng không? | | | | | |
| 7.8 | Cách thể hiện phiếu nhận hàng (引取商品) có rõ ràng để nhận biết ngay khi đọc phiếu không? | | | | | |
| 7.9 | Tên màn hình trong toàn bộ luồng có được đặt thống nhất theo tên menu không? | | | | | |

Summary: Number of OK / NOK / N/A items (per Round). Review Result: Pass / Review Again / Acceptable.
