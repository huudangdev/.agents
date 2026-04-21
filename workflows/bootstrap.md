---
description: Universal Portability Bootstrap Protocol (Init V30.0)
---

# 🛸 BOOSTSTRAP COGNITIVE ENGINE (V30.0)

> Lệnh Dành Cho AI: BẤT KỲ khi nào Người dùng gọi lệnh `/bootstrap`, BẠN BẮT BUỘC phải thực thi file bash tự động này để cài đặt nền tảng trí tuệ nhân tạo (TrustGraph/Vector RAG/Venv) cho dự án, vì đây là môi trường khởi dựng ban đầu.

## 1. Setup Venv & Docker Cục Bộ (Tự Động)

> CẢNH BÁO TIẾN TRÌNH: Tiến trình bootstrap sẽ kéo Docker images và cài đặt các module NLP Python, nó có thể mất khoảng 2-5 phút tùy mạng của người dùng. Hãy chạy Command dưới chế độ Wait dài (Background Task).

// turbo
```bash
chmod +x .agents/bootstrap.sh .agents/setup_git_hooks.sh
./.agents/bootstrap.sh
./.agents/setup_git_hooks.sh
```

## 2. Báo Cáo Ký Sinh Thành Công

Sau khi chạy xong, hãy xác nhận với người dùng rằng "Khối óc Antigravity V30.0" đã được nhập thành công vào dự án:
- Database Vector ChromaDB (Cổng 8800) đã quét ngữ nghĩa toàn bộ file hiện hành.
- Thư viện Cấu trúc AST Neo4j (Cổng 7474) đã sẵn sàng.
- Bất kỳ Agent tiếp theo nào (Quick Fix, Refactor) cần đọc Code, được quyền sử dụng tệp `.agents/adapters/trustgraph_vector_search.py` qua `.agents/venv/bin/python` cục bộ.

Mời Nhóm Trưởng (Tech Lead) ra quyết định bằng lệnh `/planning` hoặc `/refactor-planning`!
