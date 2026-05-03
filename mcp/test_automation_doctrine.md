# 🤖 Test Automation MCP Doctrine (Playwright & Selenium)

> **MỤC ĐÍCH:** Hướng dẫn LLM tư duy, tự động sinh test case, test script chuyên nghiệp cho UI/API thông qua cấu hình Playwright MCP trong `mcp.json`.

## 1. Nguyên Tắc Sinh Code Automation (End-To-End)
- **Tách Lớp Test:** Khi viết Script Playwright, BẮT BUỘC sử dụng **Page Object Model (POM)**. Không được viết locator hoặc logic click lẫn lộn vào một file test tĩnh.
- **Tính Bền Vững (Resilience):** Locator phải sử dụng `page.getByRole()`, `page.getByTestId()` hoặc `page.getByText()`. NGHIÊM CẤM TỰ DÙNG XPATH siêu cụ thể dễ đứt gãy như `//*[@id="content"]/div[2]/ul/li`.
- **Luôn Luôn Mock Data:** Ở môi trường Dev Test, mọi API ngoại bộ (Payment, Auth 3rd party) PHẢI CÓ Mock Adapter (vd: Ngăn `await page.route(...)`).

## 2. API Validation Test Scripts
- Dùng Native Node Fetch (hoặc thư viện test) bọc kèm Playwright để assert HTTP Status (phải trả 200, 201).
- Zod Integration: Chặn toàn bộ Object Body Response của API, ném vào `schema.parse()` thử nghiệm. Nếu nổ lỗi -> Đánh FAIL test case thay vì lờ đi cảnh báo TS.

## 3. Workflow Vận Hành Cùng MCP
- **Nhờ Cậy Agent `qa-simulator`:** Trong thư mục `skills/qa-simulator`, chức năng test là trọng tâm. Gọi Agent QA đọc thư mục `.agents/brain/` nội bộ để lập kịch bản Edge Cases.
- Sau khi viết xong `**.test.ts`, Agent phải dùng Tool OS để thực thi `npx playwright test --ui=false` và nhận lại report terminal. 
- Mọi Bug Terminal đều phải phân tích nguyên nhân `Root Cause` vào root `agents.md` trước khi sửa. Nếu workflow cũ vẫn trỏ vào `.agents/agents.md`, coi đó là compatibility shim chứ không phải source-of-truth.
