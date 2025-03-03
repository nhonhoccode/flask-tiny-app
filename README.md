# Tiny App Blog Documentation


## Table of Contents
- [Thông tin cá nhân](#thông-tin-cá-nhân)
- [Mô tả dự án](#mô-tả-dự-án)
- [Hướng dẫn cài đặt & chạy](#hướng-dẫn-cài-đặt--chạy)
- [Link project](#link-project)

## Thông tin cá nhân

- **Võ Trọng Nhơn** - 22658441  
- **Trần Xuân Diện** - 22650601  

## Mô tả dự án

Tiny App Blog là một ứng dụng blog được xây dựng bằng Django, cung cấp các chức năng cơ bản của một blog hiện đại.  
Các tính năng chính bao gồm:
- **Đăng ký & Đăng nhập:** Quản lý người dùng thông qua hệ thống xác thực của Django.
- **Quản lý bài viết:** Cho phép tạo, chỉnh sửa, xoá và hiển thị bài viết.
- **Tìm kiếm:** Hỗ trợ tìm kiếm bài viết theo tiêu đề hoặc nội dung.
- **Giao diện thân thiện:** Tích hợp các template để hiển thị nội dung một cách trực quan và dễ sử dụng.

Dự án được phát triển nhằm rèn luyện kỹ năng lập trình web với Django và làm nền tảng cho các ứng dụng blog phức tạp hơn trong tương lai.

## Hướng dẫn cài đặt & chạy

### Yêu cầu hệ thống
- Python 3.x  
- pip

### Các bước cài đặt

1. **Clone repository từ GitHub:**
   ```bash
   git clone https://github.com/nhonhoccode/flask-tiny-app.git
   ```

2. **Chuyển đến thư mục dự án:**
   ```bash
   cd flask-tiny-app
   ```

3. **Tạo môi trường ảo (virtual environment):**
   ```bash
   python -m venv env
   ```

4. **Kích hoạt môi trường ảo:**
   - Trên Windows:
     ```bash
     .\env\Scripts\activate
     ```
   - Trên macOS và Linux:
     ```bash
     source env/bin/activate
     ```

5. **Cài đặt các thư viện phụ thuộc:**
   ```bash
   pip install -r requirements.txt
   ```

6. **Thực hiện migrate database:**
   ```bash
   python manage.py migrate
   ```

7. **Chạy server phát triển:**
   ```bash
   python manage.py runserver
   ```

8. **Truy cập ứng dụng:**
   Mở trình duyệt và truy cập địa chỉ: [http://localhost:8000](http://localhost:8000)

## Link project

Xem chi tiết dự án tại: [https://github.com/nhonhoccode/flask-tiny-app](https://github.com/nhonhoccode/flask-tiny-app)

---

Cảm ơn bạn đã quan tâm đến dự án Tiny App Blog. Mọi ý kiến đóng góp đều được hoan nghênh để dự án ngày càng hoàn thiện hơn!