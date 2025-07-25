# Snake Game - Executable Version

## ✅ Đã sửa lỗi: Resource Path Error

Phiên bản mới đã khắc phục lỗi "FileNotFoundError: No file 'images/snake_icon.png' found" bằng cách:

- Thêm hàm `resource_path()` để xử lý đường dẫn tài nguyên đúng cách
- Cập nhật tất cả đường dẫn load hình ảnh, âm thanh và font

## Cách chạy game:

### Phương pháp 1: Chạy trực tiếp

- Mở thư mục `dist`
- Double-click vào file `SnakeGame.exe`

### Phương pháp 2: Sử dụng file batch

- Double-click vào file `run_game.bat` trong thư mục gốc

## Điều khiển game:

- Sử dụng phím mũi tên (↑↓←→) để điều khiển rắn
- Hoặc sử dụng các nút điều khiển trên màn hình (nếu bật tính năng)

## Tính năng:

- Menu cài đặt với các tùy chọn:
  - Bật/tắt phím điều khiển trên màn hình
  - Thay đổi tốc độ game (Nhanh/Chậm)
  - Bật/tắt âm thanh

## Lưu ý:

- File exe đã bao gồm tất cả tài nguyên cần thiết (hình ảnh, âm thanh, font)
- Không cần cài đặt Python hay pygame
- Có thể chạy trên máy tính khác mà không cần cài đặt gì thêm
- ✅ Đã khắc phục lỗi đường dẫn tài nguyên

## Kích thước file:

- SnakeGame.exe: ~18.3MB

## Phiên bản:

- Build mới nhất: 25/7/2025 8:50 AM
- Đã sửa lỗi resource path

Chúc bạn chơi game vui vẻ! 🐍
