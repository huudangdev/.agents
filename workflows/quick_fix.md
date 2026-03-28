---
description: Đường tắt (Bypass) để vá lỗi nhỏ hoặc thêm tính năng nhanh mà không cần phải qua dây chuyền 9 bước cồng kềnh.
---
# ⚡ THE QUICK FIX SPRINT (V29.0)

> **MỤC ĐÍCH:** Mở khóa tốc độ. Chỉ dùng tác vụ này khi Sếp gọi Fix một Bug cụ thể, đổi màu nút, hoặc thêm 1 hàm logic đơn giản trên Project ĐÃ CÓ.

// turbo-all

## 🔸 BƯỚC 1: NẠP VŨ KHÍ RAG (CONTEXT RETRIEVAL)
*🧠 Mệnh lệnh Bắt Buộc:* 
- Mở file `.clinerules` và `agents.md` để nắm hiện trạng.
- Quét nhanh `SKILLS_INDEX.md` và tuỳ ngữ cảnh gọi duy nhất **1 đến 2 SKILLS** phù hợp để tiết kiệm Token (VD: Lỗi UI -> Mở `sleek-design` hoặc `maya-ui-ux-designer`).
- Doline/Giao tiếp với thư mục `.brain/` của Component đang bị vỡ (nếu có) để nắm lý do tồn tại.

## 🔸 BƯỚC 2: MỔ XẺ VÀ CHẠY THỬ (STATIC SPRINT)
*📦 Hành Động:* Đọc Code, sửa File. 
- Mở nền Terminal Server ngầm và dùng `curl` hoặc Playwright Check đúng MỘT LẦN DUY NHẤT.
- **[Luật Circuit Breaker]:** Nếu Terminal văng lỗi đỏ, bạn chỉ được phép Fix tối đa KHÔNG QUÁ 3 LẦN LẶP LẠI (Try-Catch limit). Vượt quá 3 vòng -> Trả cờ Đỏ xin phép User. Cấm lặp vô hạn.
- **[Luật Fallback]:** Nếu các Tool Draw.io, Understand-Anything lỗi, tự chuyển sang grep và mermaid.

## 🔸 BƯỚC 3: ĐỒNG BỘ ÁM CHỈ VÀ RÚT LUI
*📦 Hành Động:* Ghi chép nội dung bạn vừa Fix, Patch, hoặc Bypass vào thẳng `agents.md` và `.brain/` của component đó. Đánh dấu [x] trong checklist. Báo cáo Sếp 1 câu ngắn gọn. Dừng hành động.
