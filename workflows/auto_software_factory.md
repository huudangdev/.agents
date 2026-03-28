---
description: Marcus Fleet Enterprise Continuous Delivery Pipeline (9-Node Directed Acyclic Graph)
---

# 🚀 CONTINUOUS SDLC DELIVERY GRAPH (V29.1)

> **MỤC ĐÍCH (PURPOSE):**  
> Đồ thị Điều phối Vòng đời Phát triển Phần mềm (Software Development Life Cycle - SDLC) này ứng dụng Phương pháp tiếp cận **Đồ thị Có hướng Không Chu trình (Directed Acyclic Graph - DAG)** để tự động hóa toàn bộ đường chuyền sản xuất từ Phân tích Đỉnh xuống Thiết kế Máy Trạng thái (FSM) và Triển khai Hợp nhất. Dưới kiến trúc V29.1, Tự Hành (Autonomous Automation) được ràng buộc nghiêm ngặt bằng cơ chế Kiểm thử Đóng cắt (Circuit Breaking) để đạt tiêu chuẩn Vercel Zero-downtime.

// turbo-all

---

## ⬛ BỘ GIAO THỨC CHỐNG SUY GIẢM BỘ NHỚ (ANTI-AMNESIA PROTOCOLS)

<identity_injection>
**LAZY-LOAD RAG ALGORITHM:** Tối ưu hóa cửa sổ Context (LLM Context Window) bằng cách ngăn chặn quá tải Identity. Tại mỗi Node, giao thức bắt buộc gọi Tool `view_file` quét Chỉ mục Khối lượng `SKILLS_INDEX.md` để trích xuất vật lý tệp `SKILL.md` của tối đa 5 Đặc vụ liên đới. Việc phỏng đoán nhân cách (Heuristic Persona Synthesis) bị đánh dấu là Lỗi Nghiêm Trọng.
</identity_injection>

<state_propagation>
**STATEFUL INHERITANCE:** Mỗi Chuyển đổi Trạng thái (State Transition) từ Node N sang Node N+1 yêu cầu Khối AI bắt buộc đọc lại (Read operation) các **[Artifacts/Outputs]** đã phát sinh từ Node N (ví dụ SDD, PRD). Dữ liệu không được phép ngắt quãng.
</state_propagation>

---

## 🔲 GRAPH TOPOLOGY: CÁC NÚT ĐIỀU PHỐI (NODES)

### ⚪ NODE 0: MÔI TRƯỜNG SANBOXED (MCP READINESS)
*🔗 Input Vector:* `.agents/mcp/mcp.json`, `agents.md`
**[Protocol]:** Kiểm định cấu hình Model Context Protocol (MCP). Bắt tay tín hiệu (Handshake) với các Server `playwright` và `drawio`. Đồng bộ Trạng thái Não bộ Cục bộ (Micro-Brain Audit) qua file `agents.md` trước khi khởi tạo Mã nguồn Tiền định.

### 🔴 NODE 1 & 2: KHÁM PHÁ THUẬT TOÁN (ALGORITHMIC DISCOVERY - PRD)
*🔗 Input Vector:* Web Search Matrix.
*🧠 Identity Injectors:* `elite6-research`, `sophia-product-manager`, `antigravity-brainstorming`, `compound-brainstorming`
*📦 Output Tensor:* Cụm PRD định dạng Phân mảnh Vật lý (Physical Segmentation).
**[Protocol]:** Đặc vụ Elite6-Research chạy vòng lặp tìm kiếm Độc lập N-Chiều. Quản trị Sản phẩm Sophia phân rã Requirement Document (PRD) thành 3 thực thể Rời rạc (Discreet Entities): `PRD_PART1_FEATURES.md`, `PRD_PART2_EDGE_CASES.md`, `PRD_PART3_SCREEN_MAP.md`. Bảng Phân bố Màn hình (Screen Map) phải ánh xạ 100% Cấu trúc Thư mục (Dir Tree), nghiêm cấm cú pháp rút gọn đa hình (`...`).

### 🟡 NODE 3: THIẾT LẬP TIỀN ĐỀ THẨM MỸ (DIGITAL AESTHETIC BASELINE)
*🔗 Input Vector:* `PRD_PART3_SCREEN_MAP.md`
*🧠 Identity Injectors:* `maya-ui-ux-designer`, `aris-designer`, `design-system-rules`
*📦 Output Tensor:* `BRAND_GUIDELINE.md`
**[Protocol]:** Trích xuất và Biên dịch Kho lưu trữ Token (Design System Tokens). Cấu hình Hierarchy cho Variables, Mixins, Global Palettes, Typography Scaling. Sản sinh Văn kiện Thẩm mỹ (Brand Guideline).

### 🟢 NODE 4: KIẾN TRÚC PHẦN MỀM CẤP CAO (ENTERPRISE ARCHITECTURE EMITTING)
*🔗 Input Vector:* PRD Edge Cases, Screen Map
*🧠 Identity Injectors:* `david-systems-architect`, `chartis-data-visualizer`, `architecture-decision-records`, `c4-architecture`, `knowledge-work-architecture`
*📦 Output Tensor:* `SDD_*.md`, Sơ đồ Ngữ nghĩa (`UML/*.md`), Vector Đồ họa (`PDF/*.pdf`)
**[Protocol]:** Kích hoạt Đặc vụ Thiết kế Backend nội tại. Tổng thể SDD bao hàm: Backend FSD, Database Schema (ERD), API Spec Contracts. Giao thức Export Tiêu chuẩn: Tool AI nhúng đoạn `classDef` cho thuật toán render Pastel Component Diagram. Chạy Binary CLI `npx -y @mermaid-js/mermaid-cli -i <file.mmd> -o <chart.png>`, sau đó tích hợp đường dẫn tĩnh Absolute Path vào Markdown và xuất PDF Trắng Đen Chuẩn hóa.

### 🔵 NODE 5 & 6: KIỂM THỬ BAN ĐẦU & RUNTIME BACKEND (ADVERSARIAL QA)
*🔗 Input Vector:* `FINAL_SPECS.md`
*🧠 Identity Injectors:* `eve-qa-approver`, `alan-tech-lead`, `ada-qa-agent`
*📦 Output Tensor:* API Stubs, Route Handlers, Database Migrations
**[Protocol]:** Khởi tạo Lớp Logic Bất Biến (Business Logic Layer) qua Unit Test Stubs (TDD Pattern). Chạy Database Migrations. Sửa lỗi dựa trên STDOUT/STDERR Console Feedback qua Bash Automata.

### 🟣 NODE 7: MÔ PHỎNG RUNTIME THỜI GIAN THỰC (LIVE FSM SIMULATION)
*🔗 Input Vector:* `BRAND_GUIDELINE.md`, `SCREEN_MAP`
*🧠 Identity Injectors:* `benny-frontend-engineer`, `qa-simulator`
**[Protocol]:** 
Kích hoạt Daemon Môi trường Sinh tồn: Gọi OS Terminal chạy lệnh `npm run dev` (Khởi động Dev Server).
- **Vòng Lặp Ghép Cặp (Bi-Directional Bi-agent Link):**
  - **Pha Render:** Biến ảo CSS/DOM (Component Rendering). Thực thi Spacing/Padding Toán học và Tuân thủ Gradient Contrast qua `benny-frontend-engineer`.
  - **Pha Mutation QA:** DOM Read & Log Capture. `qa-simulator` nạp Web Page theo Port Tương ứng. Parse SSR Hydration Errors/DOM Constraints.
  - **Cơ Chế Ngắt Mạch (V29.1 Circuit Breaker):** Phát hiện 3 Error Loop liên tiếp, Agent ngưng Render, ném Lỗi Đỏ Terminal và Báo gọi Operator User (Human-In-The-Loop). Bắt buộc Full Component Coverage trước khi Next() Node mới. Chạy tĩnh TypeScript `npx tsc --noEmit`.

### 🟤 NODE 8: TRIỂN KHAI CHUỖI KHÉP KÍN (CI/CD CLOSURE)
*🧠 Identity Injectors:* `devops-system-architect`, `ops`
**[Protocol]:** Tích hợp Kịch bản Triển khai Hạ tầng (IaC) hoặc Giao thức E2E Cypress/Playwright Ping. Ghi Error Log và Auto-Heal (tự phục hồi). Giải phóng Port Hệ thống, Khai tử Node Runtime 7.

### ⚫ NODE 9: ĐỒNG BỘ TRẠNG THÁI CỤC BỘ (MICRO-BRAIN STATE SYNC)
*🔗 Input Vector:* Progress History Context
*🧠 Identity Injectors:* Máy trạng thái Nội bộ (Butler Mode)
**[Protocol]:** Chuyển giao Graph History vào Node Theo Dõi Hành Vi `agents.md`. Tuân thủ File Append Operations tại `.brain/`. Tạo liên kết tham chiếu hai chiều thành công. Thoát Chu trình! Tắt Bộ Đếm.
