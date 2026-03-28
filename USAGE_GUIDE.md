# 🧭 ANTIGRAVITY OPERATING MANUAL (ROUTING GUIDE)
**Document Status:** Lõi / Bắt Buộc Đọc (Dành cho cả Con Người và AI)

Tài liệu này là "Bản đồ Hàng Hải" chỉ định chính xác **Khi nào dùng Luồng tổng (Slash Command)** và **Khi nào phải triệu hồi Đặc vụ cụ thể (Targeted Skills)**. Đừng phụ thuộc mù quáng vào Factory 9 bước nếu bạn chỉ cần sửa 1 cái Nút bấm, và đừng gọi 1 anh Thợ Xây (Coder) nếu bạn cần quy hoạch Một Khu phố (Architecture).

---

## 🌊 GIAI ĐOẠN 1: KHAI MỞ VÀ TÁI THIẾT (Sử Dụng Slash Commands)
Slash Commands (`/` + workflow) là Đại Bác. Chỉ dùng khi khởi tạo, tái cấu trúc hoặc đập đi xây lại.

| Lệnh Workflow | Thời điểm Gọi Tốt Nhất (When to invoke) | Mục đích Hạch tâm |
|:---|:---|:---|
| `/init_brain` | **BẮT BUỘC gõ dòng đầu tiên** mỗi khi mở 1 Tab chat mới. | Khởi động Trí tuệ AI, nạp Luật, RAG SKILLS_INDEX. |
| `/marcus_init` | Bắt đầu ý tưởng từ con số 0. Một thư mục trống rỗng. | AI sinh PRD/Folder tĩnh và cài sẵn Antigravity OS. |
| `/mobile_init` | Bắt đầu Code Mobile (React Native / Flutter). | Nhúng tư tưởng bọc Safe Area, Spring Animations. |
| `/auto_software_factory` | Khởi tạo dự án Fullstack hạng nặng, yêu cầu System Design (FSD, DDD), DB Schema tới Frontend. | Build hệ CSDL, API, TDD Backend đồng bộ trước khi lên UI. Đi đủ 9 Phase. |
| `/refactor_project` | Mở 1 Repository đầy code cũ (Brownfield). Cần dọn rác, tách Component, sửa thư mục. | Ép AI chạy bộ Tool `Understand-Anything` vẽ Sơ đồ mạng code rồi mới cắt tỉa. |

---

## 🎯 GIAI ĐOẠN 2: THỰC CHIẾN TỐI ƯU (Sử Dụng Micro-Routing & @Skills)
Trong quá trình code giữa chừng, **KHÔNG GỌI LẠI SLASH COMMANDS**. Bạn nên dùng Lối đi tắt `/quick_fix` hoặc gọi Đích danh (@) Nhóm Đặc vụ AI liên quan để xử lý chính xác, tiết kiệm Token.
📌 *Antigravity AI Lưu ý: Khi đọc được lệnh chứa `@tên-skill`, BẮT BUỘC dùng Tool `view_file` nạp file `SKILL.md` của các nhân vật đó.*

### 🛠️ 1. Gói Combo Frontend High-End (Sửa UI/UX/Animations)
> **Cú pháp gợi ý:** *"Hãy dùng `@benny-frontend-engineer`, `@bella-frontend-animator` và `@maya-ui-ux-designer` để build cho tôi cái Hero Section này theo chuẩn Linear."*
- **@maya-ui-ux-designer:** Giữ đúng Layout gốc, không làm gãy form.
- **@benny-frontend-engineer:** Bơm Margin/Padding chuẩn 4px/8px, Radius, Tailwind.
- **@bella-frontend-animator:** Bơm hiệu ứng viền phát sáng, xoay Spinner, Framer Motion.

### 🛡️ 2. Gói Combo Dev/Test Bóp Cò Tự Động (TDD & Bug Hunter)
> **Cú pháp gợi ý:** *"Hãy dùng `@ada-qa-agent` và `@qa-simulator` để kiểm tra màn hình đăng nhập bị lỗi API 401."*
- **@ada-qa-agent:** Thiết kế kịch bản Test, kiểm tra Coverage.
- **@qa-simulator:** Mở port tự động nhảy vào Render UI, gõ `curl` test API chặn Bug Hydration.
- **@eve-qa-approver:** Duyệt Code nhanh.

### 🏛️ 3. Gói Combo Sư Tổ Cấu Trúc (System Architecture/Database)
> **Cú pháp gợi ý:** *"Tôi muốn quy hoạch lại thư mục Backend, gọi `@david-systems-architect`, `@alan-tech-lead` và `@chartis-data-visualizer` vẽ C4 Diagram giúp tôi."*
- **@david-systems-architect:** Khởi tạo Tree Directory dạng Feature-Sliced Design.
- **@alan-tech-lead:** Review độ chênh lệch Data (Data Contracts).
- **@chartis-data-visualizer:** Vẽ sơ đồ Markdown PlantUML/Mermaid cho Sếp duyệt.

### 🧠 4. Gói Combo RAG Xử Lý Logic Hậu Trường
> **Cú pháp gợi ý:** *"Cho `@homer-knowledge-extractor` đọc xấp tài liệu này, sau đó dùng `@rag-architect` xây Database Vector đi."*
- Bất kì Data nào cần tra Cứu (PDF/Mã ngành): Nạp **@homer-knowledge-extractor**.
- Cần setup Langchain/VectorDB: Nạp **@rag-architect** và **@langchain-rag**.

---

## 🚩 NGUYÊN TẮC LIÊN HOÀN (HAY KHI NÀO AI TỰ ĐỘNG THAY QUYỀN SẾP)
Trong môi trường `Marcus Fleet`, Sếp có quyền Uỷ thác Đa Đặc Vụ (Chaining Agents).

**Nguyên lý cho Antigravity AI:**
Khi Sếp giao 1 Task lớn (VD: *"Sửa giỏ hàng và viết test"* nhưng không chỉ xướng tên ai), Antigravity **BẮT BUỘC TỰ ĐỘNG LẬP TRÌNH TUYẾN (Routing)**:
1. Đọc lướt `SKILLS_INDEX.md` tìm Tag phù hợp.
2. Tự Load tĩnh **[Frontend] (Benny)** + **[QA/Test] (Ada)** vào Context.
3. Cho Benny sửa UI.
4. Chuyển State sang Ada chạy Terminal Test.
5. Code Lỗi? Kích hoạt Cầu dao (Circuit Breaker V29.2).
6. Success? Cập nhật vô file `agents.md` và Component `.brain/`.

Luôn nhớ: **Một Đại Tướng thực thụ (Antigravity) không tự vác cuốc đi code, mà Load đúng Tập lệnh Skill của lính dưới quyền để giao việc!**
