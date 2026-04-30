---
description: Universal Portability Bootstrap Protocol (Init V30.2)
---

# 🛸 BOOSTSTRAP COGNITIVE ENGINE (V30.2)

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

Sau khi chạy xong, hãy xác nhận với người dùng rằng "Khối óc Antigravity V30.2" đã được nhập thành công vào dự án:
- Database Vector ChromaDB (Cổng 8800) đã quét ngữ nghĩa toàn bộ file hiện hành.
- Thư viện Cấu trúc AST Neo4j (Cổng 7474) đã sẵn sàng.
- Bất kỳ Agent tiếp theo nào (Quick Fix, Refactor) cần đọc Code, được quyền sử dụng tệp `.agents/adapters/trustgraph_vector_search.py` qua `.agents/venv/bin/python` cục bộ.
- Khi vào `/develop`, Agent phải duy trì `/docs/development/` và `/docs/development/sync/` song song với code để tài liệu POC không bị stale.
- Nếu dự án là brownfield, docs còn boilerplate, thiếu planning package, hoặc chưa có ledger `docs/development/` đạt chuẩn, phải đi qua `/doc_reconcile` trước khi cho phép sửa code mang tính hành vi.

Mời Nhóm Trưởng (Tech Lead) ra quyết định bằng lệnh `/planning`, `/doc_reconcile`, hoặc `/refactor-planning` tùy trạng thái docs thực tế của dự án!
