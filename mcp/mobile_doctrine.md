# 📱 Antigravity Mobile Design Doctrine (MCP Reference)

> **MỤC ĐÍCH:** Bộ quy tắc cốt lõi giúp hệ thống AI tự động review kiến trúc & UX iOS/Android, cũng như quyết định công nghệ (RN/Flutter/Native) theo tiêu chí Performance và Offline-first.

## 1. Quyết định Tech Stack (Architectural Decision)
- **Nếu ưu tiên Performance Native & Animation (60-120fps):** Chọn React Native (viết bằng Expo Router, Reanimated 3) hoặc Swift Native (cho iOS only).
- **Nếu app cồng kềnh, UI siêu custom & Không dùng OS Native features nhiều:** Chọn Flutter.
- **Offline-First:** Bắt buộc áp dụng WatermelonDB (RN) hoặc Isar (Flutter) có Sync Engine.

## 2. Tiêu chuẩn UX/UI Mobile (Sleek Taste)
- **Touch Targets:** Tối thiểu 44x44pt cho iOS và 48x48dp cho Android.
- **Micro-interactions:** Mọi click button phải có hiệu ứng nhún lò xo (Spring damping: 15, stiffness: 200). KHÔNG dùng hiệu ứng mờ (Opacity) nhàm chán.
- **Safe Area:** 100% Navbar và Bottom Tab phải né Tai thỏ (Notch) & Thanh Home (Home Indicator) - Dùng `SafeAreaProvider`.
- **Keyboard Handling:** Form nhập liệu BẮT BUỘC có `KeyboardAvoidingView` + `ScrollView` đẩy UI lên, tuyệt đối không để bàn phím che khuất Input.

## 3. Kiến trúc Component & Testing
- Chia tách logic theo **FSD (Feature-Sliced Design)**. API calls đưa vào thư mục `shared/api` để tái sử dụng.
- Dùng **Playwright MCP** (cấu hình trong `mcp.json`) để mô phỏng End-to-End Test API đằng sau UI. App Mobile cần được mock dữ liệu cẩn thận.
