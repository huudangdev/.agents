---
description: Khởi động đồ thị Understand-Anything và Audit toàn diện codebase cho cấu trúc cũ.
---

# 🛠️ GIAO THỨC REFACTOR MỞ RỘNG TỪ BỘ HIỂU (UNDERSTAND-ANYTHING)

> **MỤC ĐÍCH:** Áp dụng cho các dự án "Brownfield" (đã có source) / dự án lớn cồng kềnh mất kiểm soát.

// turbo-all

## ⚪ STAGE 1: TẠO BRAIN GRAPH (HIỂU SOURCE)
*🧠 Mệnh lệnh Bắt Buộc:* Gọi tool OS Terminal chạy `npx understand-anything` để sinh ra bản đồ Knowledge Graph của toàn dự án (phân tích file, hàm, class).
Đồng thời nạp `understand-chat`, `understand-diff` (nếu có update repo) để thẩm thấu kiến trúc.

## ⚪ STAGE 2: ADAPTIVE ARCHITECTURE
*🧠 KỸ NĂNG: Đọc file `agents.md`, `architecture.md` và tuân thủ các plugins: `improve-codebase-architecture`, `refactor-copilot`, `refactor-plan`, `refactor-complexity` và `refactor-review`.*
*📦 Hành Động:* Giảm thiểu độ phức tạp của component (Complexity reduction). Băm siêu nhỏ theo FSD.

## ⚪ STAGE 3: TEST PHẢN ỨNG NỔ (QA SIMULATION)
*🧠 KỸ NĂNG: `playwright-test`, `qa-simulator`, `ops`*
*📦 Hành Động:* Viết test script Playwright và quét cURL/DOM kiểm chứng lại logic app chưa vỡ sau khi refactor. Bắt buộc Mở Server Ngầm.

## ⚪ STAGE 4: CẬP NHẬT LỊCH SỬ REFACTOR VÀO AGENTS.MD
*📦 Hành Động:* Lưu lại những Node đã đổi tên, gỡ rối, module tách file vào `agents.md`. Giao tiếp với não bộ của `.brain/` nội bộ.
