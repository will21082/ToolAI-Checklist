# POS UI — Checklist Thiết kế màn hình (từ comment Backlog 2026-05-22)

| Mục | Giá trị |
|---|---|
| Mã tài liệu VTI | 09-CL/PM/VTI |
| Phiên bản | 1.0 |
| Dự án | POS_UI — Quản lý UI POS máy tính bảng (タブレットPOS UI管理) |
| Backlog Domain | siconnect.backlog.com |
| Nguồn dữ liệu | Comment trong ngày 2026-05-22 (6 comments / 6 issues, không lọc tác giả) |
| Ngày tạo | 2026-05-22 |

---

## Lịch sử thay đổi

| STT | Ngày | Phiên bản | Người phụ trách | Nội dung thay đổi | Người review | Người duyệt |
|---|---|---|---|---|---|---|
| 1.0 | 2026/05/22 | 1.0 | Auto-generated | Tự sinh từ comment Backlog | | |

---

## Checklist các rule

| # | Màn hình (Issue) | Phân loại | Đối tượng | Rule kiểm tra | Round 1 | Round 2 | Round 3 | Bắt buộc | Comment ID | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Nhập người phụ trách — C000091 (POS_UI-138) | Label / Nhãn | Nhãn người phụ trách | Hiển thị nhãn là **"Người nhập" (入力担当者)**, KHÔNG dùng "Người phụ trách bán hàng" (販売担当者) | | | | ○ | 741507347 | Đổi nhãn từ "販売担当者" → "入力担当者" trên màn nhập người phụ trách |
| 2 | Mới / Báo giá thiết bị — C000093 (POS_UI-143) | Label / Nhãn | Nút "Báo giá thiết bị" | Tên nút phải đổi thành **"Tìm kiếm báo giá" (見積書検索)**, không dùng "Báo giá thiết bị" (端末見積) | | | | ○ | 741547734 | Đổi tên button "端末見積" → "見積書検索" |
| 3 | Mới / Báo giá thiết bị — C000093 (POS_UI-143) | Layout & Size | Vùng "Chọn loại báo giá" (見積種類選択) | **Xoá** vùng "Chọn loại báo giá" đang đặt ở vị trí trên cùng màn hình | | | | ○ | 741547734 | Bỏ phần "見積種類選択" ở top màn hình |
| 4 | Mới / Báo giá thiết bị — C000093 (POS_UI-143) | Hiển thị dữ liệu | Câu hướng dẫn | Vị trí trên cùng phải hiển thị câu hướng dẫn yêu cầu user chọn giữa **"Báo giá mới" (新規見積)** hoặc **"Tìm kiếm báo giá" (見積書検索)** | | | | ○ | 741547734 | Câu hướng dẫn chọn giữa 2 nút thay cho block "見積種類選択" đã bị xoá |
| 5 | Tìm kiếm trạng thái giao hàng — XXXXX (POS_UI-213) | Hành vi component | Icon "con mắt" (目のマーク) | Khi chạm icon **"con mắt"** → hiển thị popup **"Thông tin đăng ký"** theo đúng layout đính kèm | | | | ○ | 741457089 | Khi tap icon eye sẽ mở màn hình đăng ký thông tin |
| 6 | Tìm kiếm trạng thái giao hàng — XXXXX (POS_UI-213) | Hành vi component | Nút **"Tìm thêm" (もっと検索)** | Khi chạm nút "Tìm thêm" → **thu gọn** vùng điều kiện tìm kiếm, đồng thời **tăng số dòng** hiển thị ở list chi tiết tương ứng | | | | ○ | 741457089 | Tap nút → collapse khu vực filter để mở rộng list data |

---

## Comment KHÔNG sinh rule (chỉ là phản hồi trạng thái)

| # | Issue | Comment ID | Tác giả | Nội dung tóm tắt | Lý do bỏ qua |
|---|---|---|---|---|---|
| A | Nhập mô tả — C000096 (POS_UI-142) | 741514315 | VTI アイン | "Cảm ơn góp ý. Đã sửa xong." | Chỉ là xác nhận đã sửa — rule gốc nằm ở comment trước đó của khách |
| B | DS điểm giao hàng — XXXXX (POS_UI-214) | 741451602 | VTI アイン | "Đã reflect lên Figma, vui lòng review bản mới nhất." | Thông báo update Figma, không kèm rule cụ thể |
| C | Nhập người phụ trách — C000091 (POS_UI-220) | 741577692 | VTI アイン | "Đã thêm design màn nhập người phụ trách." | Thông báo thêm design, không kèm rule cụ thể |

---

## Phụ lục: comment gốc (full — giữ nguyên tiếng Nhật để truy vết)

### [POS_UI-138 / 741507347] C000091_担当者入力 — VTI アイン @ 2026-05-22 01:51 UTC
```
@SMJ 河野 CC: @
ご指摘ありがとうございます。「販売担当者」から「入力担当者」へ修正いたしました。
ご確認のほどよろしくお願いいたします。
```
**Dịch nhanh:** Cảm ơn góp ý. Đã sửa "Người phụ trách bán hàng" thành "Người nhập". Vui lòng review.

### [POS_UI-142 / 741514315] C000096_摘要入力 — VTI アイン @ 2026-05-22 01:56 UTC
```
@SMJ 河野 cc: @VTI ゴク
ご指摘ありがとうございます。修正いたしました。
ご確認のほどよろしくお願いいたします。
```
**Dịch nhanh:** Cảm ơn góp ý. Đã sửa xong. Vui lòng review.

### [POS_UI-143 / 741547734] C000093_新規 or 端末見積 — VTI アイン @ 2026-05-22 02:21 UTC
```
@SMJ 河野 cc: @VTI ゴク
ご指摘ありがとうございます。
下記の通り対応いたしましたので、ご確認のほどよろしくお願いいたします。
・「端末見積」を「見積書検索」へ変更いたしました。
・最上部に配置していた「見積種類選択」を削除いたしました。
上記対応により、最上部に「新規見積」ボタンまたは「見積書検索」ボタンを選択する
説明文が配置される構成となっております。
ご確認のほどよろしくお願いいたします。
```
**Dịch nhanh:** Cảm ơn góp ý. Đã xử lý như sau:
- Đổi "Báo giá thiết bị" thành "Tìm kiếm báo giá".
- Xoá vùng "Chọn loại báo giá" ở top.
- Kết quả: top màn hình hiển thị hướng dẫn user chọn giữa "Báo giá mới" hoặc "Tìm kiếm báo giá".

### [POS_UI-213 / 741457089] XXXXX 配送状況照会検索 — VTI アイン @ 2026-05-22 01:14 UTC
```
@SMJ 河野 cc: @VTI ゴク
ご確認いただいた内容をFigmaに反映し、最新版をアップいたしました。

また、「目のマーク」についてご質問いただいた件ですが、以下の仕様としております。
・目のマークをタッチすると、添付画像のような登録情報画面が表示されます。

![image][pasted-2026.05.22-10.13.43.png]

・「もっと検索」ボタンをタッチすると検索条件部が収納（短縮）され、
  その分明細行が増えるイメージです。

お手数ですーが、ご確認のほどよろしくお願いいたします。
```
**Dịch nhanh:** Đã reflect lên Figma bản mới. Spec icon "con mắt":
- Tap → mở màn hình "Thông tin đăng ký" như ảnh đính kèm.
- Nút "Tìm thêm" tap → thu gọn vùng điều kiện, tăng số dòng list chi tiết.

### [POS_UI-214 / 741451602] XXXXX 配送状況照会訪問先一覧 — VTI アイン @ 2026-05-22 01:09 UTC
```
@SMJ 河野 cc: @VTI ゴク
ご依頼いただいた内容をFigmaに反映し、最新版をアップいたしました。
お手数ですが、ご確認のほどよろしくお願いいたします。
```
**Dịch nhanh:** Đã reflect yêu cầu lên Figma. Vui lòng review.

### [POS_UI-220 / 741577692] C000091_担当者入力 — VTI アイン @ 2026-05-22 02:45 UTC
```
@SMJ 河野 cc: @VTI ゴク
担当者入力画面のデザインを追加いたしました。ご確認のほどよろしくお願いいたします。
```
**Dịch nhanh:** Đã thêm design cho màn nhập người phụ trách. Vui lòng review.

---

## Ghi chú quan trọng

- **Cả 6 comment hôm nay đều là reply của team VTI (アイン)**, không phải comment gốc của khách (SMJ 河野). Rule trích ra ở đây phản ánh "trạng thái design **sau khi đã sửa** theo yêu cầu khách". Nếu cần xem rule gốc khách yêu cầu (trước khi VTI sửa) → cần kéo thêm comment trước đó của 河野 trên cùng issue.
- 3 comment (POS_UI-142, 214, 220) chỉ là thông báo trạng thái (đã sửa / đã upload Figma / đã thêm design), không kèm chi tiết rule cụ thể → liệt kê riêng ở section "không sinh rule".
- Cột **Bắt buộc** mặc định là `○`. Chưa có comment nào dùng từ `必須 / 必ず / 必要があります` (bắt buộc, nhất định, cần phải) để nâng lên `◎`.
- Cột **Round 1 / 2 / 3** để trống cho designer tự điền `◯ / ✕ / −` khi review từng vòng.
- Thuật ngữ tiếng Nhật được giữ trong ngoặc để designer dễ đối chiếu với Figma / màn hình thực tế.
