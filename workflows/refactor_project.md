---
description: Khởi động Đồ thị Truy Xuất Biểu Đồ (Understand-Anything) và Tái thiết Mã nguồn Kế thừa
---

# 🛠️ GIAO THỨC ĐỒNG HÓA VÀ RÃ CẤU TRÚC KẾ THỪA (AST HOMOGENIZATION PROTOCOL)

> **MỤC ĐÍCH (PURPOSE):**  
> Giao thức này định hình khuôn mẫu cho việc thẩm thấu và tái cấu trúc các Dự án Kế thừa (Brownfield / Legacy Projects) bị phình to (Code Bloat) hoặc sai lệch thiết kế kiến trúc. Thay vì chỉnh sửa mù quáng, Antigravity AI áp dụng Hệ thống Đồ thị Tri thức (Knowledge Graph) để ánh xạ Sự phụ thuộc (Dependency Injection Mapping) trước khi tiến hành cắt tỉa Mã Mì Ý (Spaghetti Code).

// turbo-all

---

## 🟢 STAGE 1: KHỞI TẠO ĐỒ THỊ TRI THỨC VÀ ÁNH XẠ CÚ PHÁP (AST EXTRACTION)
*🧠 Skill Injection (Bắt buộc):* Nạp các Plugin hiểu biết bao gồm `understand-chat`, `understand-diff` (đối với việc phân tích Pull Request/Diff).
1. **[Lệnh Gọi Hệ thống]:** Kích hoạt hệ điều hành (OS Terminal) gọi công cụ `npx understand-anything`. Phân tích và sinh ra cây đồ thị trừu tượng (Abstract Syntax Tree) và Bộ điều hướng cho toàn bộ Dự án.
2. Từ lúc này, Não bộ AI đã liên kết mọi Node liên quan đến Class, Component React, Services Backend, và Cây Thư mục. Nghiêm cấm mọi hành vi thao tác File khi chưa quét qua mạng lưới Graph này.

## 🟡 STAGE 2: KIẾN TRÚC THÍCH ỨNG & GIẢM ĐỘ PHỨC TẠP (COMPLEXITY ALLEVIATION)
*🧠 Skill Injection (Bắt buộc):* Đọc file `.brain/agents.md`, `docs/architecture.md` (nếu có). Nạp các plugin chuyên sâu: `improve-codebase-architecture`, `refactor-copilot`, `refactor-plan`, `refactor-complexity` và `refactor-review`.
1. **[Codebase Pruning]:** Rà soát độ phức tạp biểu đồ vòng (Cyclomatic Complexity). Phân rã (De-couple) các File `>300 dòng` thành các mảnh FSD (Feature-Sliced Design).
2. Tách Biến trạng thái (State Hook) và Dữ liệu thuần (Pure Function). Đặt Lớp Giao tiếp (Service Layer) làm bức tường lửa cho Logic UI.

## 🟠 STAGE 3: MÔ PHỎNG KIỂM THỬ XUNG KÍCH (QA SIMULATION & DOM MUTATION)
*🧠 Skill Injection (Bắt buộc):* `playwright-test`, `qa-simulator`, `devops-system-architect` (hoặc `ada-qa-agent`)
1. **[Runtime Verifications]:** Sau quá trình cắt tỉa, Rủi ro Hệ thống đổ vỡ (Regress Bug Breakage) là cực kỳ cao. Bắt buộc Mở Phiên Chạy Ngầm (Daemon Server).
2. Đặc vụ Viết các Kịch bản Automation Testing qua Playwright. Mô phỏng luồng Click Của Người Dùng. Quét cURL/DOM Validation. Cấm kết luận "Refactor Xong" nếu chưa nhận được tín hiệu OK từ Terminal.

## 🔵 STAGE 4: ĐỒNG BỘ TRẠNG THÁI MUTATIONS (HISTORY SYNCHRONIZATION)
*📦 Artifact Update:* File `agents.md` & `/docs/`
1. Đảo ngược trạng thái, ghi log sự thay đổi về Node. Cập nhật các Component bị Rename, Tách Class, Đổi Dependency Router. Ghi vào Sổ theo dõi Lịch sử của Micro-Brain tại `agents.md`.
2. Trả mã Exit Code Xanh để hoàn tất quy trình Refactor Khép kín.
