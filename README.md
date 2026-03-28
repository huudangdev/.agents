# 🚀 Marcus Fleet Enterprise Matrix (.agents)
**Phiên bản:** Antigravity V29.1 - The Dynamic Lazy-Loading Epoch

**The Ultimate AGI Core for Software Architecture, FSD/DDD Coding, Pixel-perfect UI/UX, and Autonomous DevOps.**

Đây là bộ Lõi Phân tán (Distributed Brain) mạnh mẽ nhất. Khác với các mô hình prompt tĩnh truyền thống, **V29.1** đã tiến hóa thành một "Sandbox Động": Chạy tác vụ Tĩnh/Động xen kẽ, tự động RAG nạp kỹ năng, có Circuit Breaker bảo vệ API và sở hữu kho tàng **64 Đặc Vụ Tinh Anh**. 

Hệ thống chạy 100% tự động, KHÔNG viết tắt code (Zero-Truncation) và KHÔNG bắt user tự gõ lệnh CLI.

---

## 🏗️ KIẾN TRÚC HOẠT ĐỘNG V29.1 (Visual Workflow)

```mermaid
graph TD
    User([Sếp / Con Người]) --> |Nhập Slash Command| AgentCore{Antigravity Core}
    
    subgraph "Federal Brain Matrix (Core Lõi)"
    AgentCore --> |1. Lazy-Loading| RAG[🧠 SKILLS_INDEX.md]
    RAG --> |2. Lấy 5-7 Skills / 64| Context[LLM Context Window]
    end
    
    subgraph "System Tools & Guards"
    Context --> |3. Thực thi| Code[Code Editor / Terminal]
    Code --> |Lỗi Limit 3 Tự Ngắt| CircuitBreaker[Cầu Dao Bảo Vệ]
    CircuitBreaker -.-> |Human-in-the-Loop| User
    Context --> |4. Tool Lỗi?| Fallback[Fallback Tools - Mermaid / Grep]
    end
    
    subgraph "Workflows"
    Context --> W1[/quick_fix]
    Context --> W2[/auto_software_factory]
    Context --> W3[/refactor_project]
    end
```

---

## 🌟 TÍNH NĂNG ĐỘT PHÁ TỪ V29.1
1. **Semantic RAG Lazy-Loading:** Không tải toàn bộ 64 thư mục vào Memory làm tràn RAM và gây ảo giác (Hallucination). Antigravity tự đọc `SKILLS_INDEX.md`, tìm Tag `[Frontend]`, `[QA]`, `[Architecture]` và Nạp đúng người đúng việc. Gíup tăng 80% tốc độ khởi chạy.
2. **Circuit Breaker (Mạch ngắt 3 Try):** Nếu AI vấp bug Terminal và cố fix lỗi tới lần thứ 3 mà vẫn thất bại -> Hệ thống TỰ ĐỘNG CÚP ĐIỆN, giương Cờ Đỏ (🚩) gọi Sếp vào xử lý. Bảo vệ Tuyệt Đối số dư tài khoản Token của bạn.
3. **Mạng lưới Nhớ Cục Bộ (Micro-Brain):** Hệ thống không bao giờ bị mất trí nhớ. Mọi quyết định đều được ghi chép vào `agents.md` và `.brain/` của dự án.
4. **Hệ Thống Phản Ứng Phụ (Tool Fallback):** Khi Server vẽ Graph (Draw.io, Understand-Anything) bị sập -> AI tự lùi về code Mermaid Markdown tĩnh hoặc Grep Shell native. Cương quyết không nói "Tôi không làm được".

---

## 📦 CÁCH CÀI ĐẶT
Để sử dụng bộ Não này cho các dự án của bạn, chỉ cần tạo một Workspace tổng, sau đó clone kho chứa AI Core về máy.

```bash
# 1. Tạo một thư mục Workspace tổng cho công ty/cá nhân
mkdir marcus-workspace && cd marcus-workspace

# 2. Clone "Lõi AI" Marcus Fleet về (dưới Tên thư mục ẩn .agents)
git clone https://github.com/huudangdev/.agents.git .agents

# 3. Mở mã nguồn bằng Cursor / OpenClaw / Antigravity và trải nghiệm.
```

> **📖 ĐỌC NGAY:** Trước khi bắt tay vào code, BẮT BUỘC đọc [HƯỚNG DẪN HÀNG HẢI TỐI THƯỢNG (USAGE_GUIDE.md)](./USAGE_GUIDE.md) để biết chính xác khi nào dùng Lệnh Tổng (`/commands`), khi nào dùng Combo Chỉ Huy (`@skills`).

---

## ⚡ CÁC LỆNH TỐI THƯỢNG (SLASH COMMANDS)
Hệ thống được thiết kế để tự động hóa vật lý mọi thao tác tay của lập trình viên. Bạn CHỈ CẦN GÕ COMMAND vào khung chat của AI như một Terminal Console thực thụ:

### 1. 🟢 Lệnh Bắt Buộc: Cấp Nguồn Não Bộ
> Gõ: `/init_brain`
- **Mục đích:** Đánh thức 64 Đặc vụ. Nạp Bách khoa toàn thư Nghữ nghĩa (Semantic Index) và Đạo luật `.clinerules`. 
- **Khi nào dùng:** MỌI KHI BẠN BẮT ĐẦU MỘT ĐOẠN CHAT MỚI. Khởi động Lạnh để tránh Trí tuệ ảo bị ảo giác.

### 2. 🟡 Nhảy Cóc Tốc Độ: Luồng Fix Bug Siêu Nhanh (Ninja Bypass)
> Gõ: `/quick_fix`
- **Mục đích:** Bỏ qua hoàn toàn bộ máy phân tích, vẽ sơ đồ, viết PRD. Nhảy thẳng vào Bug. Áp dụng sửa giao diện (Đổi màu Nút, Sửa Border, Thêm API field).
- **Quy trình:** AI RAG đúng duy nhất 1 Đặc vụ ➔ Sửa Tĩnh ➔ Run Terminal Test ➔ Lưu History ➔ End. Quá trình xử lý: ~ 4 Phút.

### 3. 🔴 Cỗ Máy Công Nghiệp Nặng: Auto Software Factory
> Gõ: `/auto_software_factory`
- **Mục đích:** Setup một khung sườn (Monorepo, Web, Backend) hoàn toàn mới hoặc viết một Tính năng Fullstack siêu lớn.
- **Quy trình 9 Bước Nặng Đô:** 
  Dựng Architecture (FSD/DDD) -> Giao việc cho PM viết PRD -> Vẽ Diagram C4 -> Dev Code TDD -> Chạy Playwright E2E -> Push DB. 

### 4. 🔵 Tân Trang Mã Nguồn (Refactoring)
> Gõ: `/refactor_project`
- **Mục đích:** Dành cho dự án Cũ kĩ, bừa bộn rác (Brownfield).
- **Quy trình:** Bắt buộc AI chạy `npx understand-anything` để vẽ Knowledge Graph 100% kho Source code, tính toán mức độ Complexity, rồi mới được quyền băm đập Code để đập đi xây lại.

### 5. 🟣 Đặc Vụ Mobile Thần Thánh
> Gõ: `/mobile_init`
- **Mục đích:** Giao toàn quyền sinh sát cho học thuyết **Mobile Design Doctrine**.
- **Quy trình:** Ép UI/UX phải theo chuẩn iOS/Tailwind, bọc Safe-area toàn app, cấy các hiệu ứng Touchable-Spring-Animations (Phản ứng lò xo khi chạm vào nút).

---

## 🔒 LUẬT THÉP TỰ TRỊ (ZERO SUGGESTION POLICY)
Bất kỳ LLM nào được nhúng vào `.agents` này đều bị TƯỚC ĐOẠT quyền năng **"Gợi ý lệnh (Suggestion)"**. 

Nó KHÔNG BAO GIỜ được phép Copy/Paste đoạn code Bash ra khung Chat rồi bảo *"Bạn hãy dán lệnh này vào terminal nhé"*. 
Nó **BẮT BUỘC** phải dùng Core Tools của máy chủ để tự ấn phím, tự Build, tự Debug và chỉ trả cái Gật Đầu Hoàn Thiện cho Bạn!
