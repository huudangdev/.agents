---
description: Marcus Fleet Startup Matrix (Tự động Scaffold Dự án, clone Agents & Gen Spec)
---
# 🚀 MARCUS FLEET - SUPREME PROJECT KICKSTARTER

Workflow này sinh ra để xóa sổ 100% các thao tác tay dư thừa (Tạo Folder, Tạo File Spec, Copy Paste `.agents`...). Khi Sếp gọi lệnh này, Antigravity BẮT BUỘC phải làm thay toàn bộ bằng quyền truy cập OS.

> **HƯỚNG DẪN THỰC THI CHO ANTIGRAVITY:**

1. **Phân tích Input:** Nếu trong câu lệnh của Sếp đã có <Tên Dự Án> và <Mô tả chức năng>, hãy lấy nội dung đó. (Nếu chưa có, hãy lịch sự hỏi Sếp trước khi sang Bước 2).

// turbo
2. **Scaffold Hệ Sinh Thái (Vật Lý):** Bạn BẮT BUỘC dùng Tool `run_command` chạy Bash Script sau để tạo Cấu trúc thư mục chuẩn và Clone toàn bộ Lõi AI sang dự án mới:
    ```bash
    export PROJECT_NAME="<Tên_Dự_Án_Viết_Liền_Chữ_Thường_Hoặc_Gạch_Ngang>"
    mkdir -p projects/$PROJECT_NAME/docs
    cp -r .agents projects/$PROJECT_NAME/
    cp .agents/.clinerules projects/$PROJECT_NAME/.clinerules
    ```

3. **Khởi tạo Dữ Liệu Não Bộ:** Sử dụng Tool `write_to_file` để sinh ra file Spec Gốc:
    - **Đường dẫn mục tiêu:** `projects/<Tên_Dự_Án>/docs/PRD_RAW.md`
    - **Nội dung:** Bơm toàn bộ ý tưởng / yêu cầu của Sếp vào file này dưới dạng gạch đầu dòng Markdown rõ rệt. Đừng bỏ sót một từ nào sếp đã nhắn.

4. **Bàn Giao & Khai Hoả:** Sau khi chạy xong, hãy thông báo Báo Cáo Triển Khai thành công rực rỡ và hướng dẫn (hoặc tự động tuỳ quyền hạn) Sếp dịch chuyển Workspace:
    > "Dự án đã được Setup cấu trúc Mẹ thành công. Sếp chỉ cần nhảy vào thư mục `cd projects/<Tên_Dự_Án>` và gõ lệnh `/auto_software_factory` là Tòa Án AI sẽ lập tức thi hành!"
