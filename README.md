Dưới đây là bản cập nhật README.md hoàn chỉnh hơn, logic mạch lạc hơn, thêm icon đẹp mắt và cập nhật chi tiết việc sử dụng Docker (có sẵn Dockerfile và docker-compose.yml):

---

# 🚀 Tiny App Blog Documentation

---

## 📖 Mục lục
- [👤 Thông tin cá nhân](#-thông-tin-cá-nhân)
- [💡 Mô tả dự án](#-mô-tả-dự-án)
- [🛠️ Hướng dẫn cài đặt & chạy](#️-hướng-dẫn-cài-đặt--chạy)
- [🐳 Hướng dẫn triển khai với Docker](#-hướng-dẫn-triển-khai-với-docker)
- [🌐 Link triển khai project](#-link-triển-khai-project)

---

## 👤 Thông tin cá nhân

- **Võ Trọng Nhơn** - `22658441`  
- **Trần Xuân Diện** - `22650601`

---

## 💡 Mô tả dự án

**Tiny App Blog** là một ứng dụng web blog hoàn chỉnh được xây dựng bằng Django. Dự án hướng đến việc cung cấp các chức năng quản lý nội dung cơ bản của blog và đồng thời phát triển thêm một số tính năng quản trị người dùng nâng cao, đáp ứng các yêu cầu thực tế của một ứng dụng web hiện đại.

### 🔥 Các tính năng chính:

- ✅ **Đăng ký & Đăng nhập** người dùng.
- 📄 **Quản lý bài viết** cá nhân (tạo, sửa, xóa).
- 🔎 **Tìm kiếm bài viết** dễ dàng, nhanh chóng.
- 🎨 **Giao diện thân thiện, trực quan**.

### 🚧 Lộ trình phát triển theo các phiên bản:

- 🌟 **Version 2**:  
  - Tính năng đăng nhập/đăng ký nâng cao, bảo mật hơn.

- 🌟 **Version 3**:  
  - Thêm trang **Admin** quản lý người dùng:
    - Cho phép Admin **khóa (block)** tài khoản và **reset mật khẩu**.
    - Thông báo rõ ràng khi tài khoản bị khóa: _"Tài khoản của bạn đã bị khóa"_.

- 🌟 **Version 4**:  
  - User quản lý bài viết hiệu quả hơn:
    - Cho phép user **xóa đồng thời nhiều bài viết** cùng lúc.

- 🌟 **Version 5**:  
  - Triển khai tính năng **phân trang (pagination)** cho bài viết, hiển thị số lượng bài viết giới hạn trên mỗi trang.

---

## 🛠️ Hướng dẫn cài đặt & chạy (không Docker)

### ⚙️ Yêu cầu hệ thống

- 🐍 Python 3.x  
- 📦 pip (Package Installer)

### 📌 Các bước cài đặt:

1. **Clone repository từ GitHub**
```bash
git clone https://github.com/nhonhoccode/flask-tiny-app.git
cd flask-tiny-app
```

2. **Tạo và kích hoạt môi trường ảo**
```bash
python -m venv env
```

- Windows:
```bash
.\env\Scripts\activate
```

- macOS/Linux:
```bash
source env/bin/activate
```

3. **Cài đặt các package cần thiết**
```bash
pip install -r requirements.txt
```

4. **Khởi tạo database**
```bash
python manage.py migrate
```

5. **Chạy ứng dụng**
```bash
python manage.py runserver
```

6. **Truy cập website**
- 🌐 Mở trình duyệt và truy cập [http://localhost:8000](http://localhost:8000)

---

## 🐳 Hướng dẫn triển khai với Docker

> 🔹 Dự án cung cấp sẵn **Dockerfile** và **docker-compose.yml** giúp bạn dễ dàng triển khai.

### 📌 Cách 1: Chạy với Dockerfile trực tiếp

1. **Clone repository**
```bash
git clone https://github.com/nhonhoccode/flask-tiny-app.git
cd flask-tiny-app
```

2. **Build Docker image**
```bash
docker build -t tiny-app-blog .
```

3. **Chạy container**
```bash
docker run -d -p 8000:8000 tiny-app-blog
```

4. **Truy cập ứng dụng**
- 🌐 [http://localhost:8000](http://localhost:8000)

---

### 📌 Cách 2: Chạy nhanh với Docker Compose (khuyên dùng)

1. **Clone repository**
```bash
git clone https://github.com/nhonhoccode/flask-tiny-app.git
cd flask-tiny-app
```

2. **Build và khởi chạy tất cả container**
```bash
docker-compose up --build -d
```

3. **Kiểm tra trạng thái các container**
```bash
docker-compose ps
```

4. **Truy cập ứng dụng**
- 🌐 [http://localhost:8000](http://localhost:8000)

5. **Dừng và xoá các container**
```bash
docker-compose down
```

---

## 🌐 Link triển khai project

- 💻 **GitHub Repository**:  
[https://github.com/nhonhoccode/flask-tiny-app](https://github.com/nhonhoccode/flask-tiny-app)

- 🚀 **Link triển khai thực tế**:  
_(coming soon)_

---

🙌 **Cảm ơn bạn đã quan tâm đến dự án Tiny App Blog!**  