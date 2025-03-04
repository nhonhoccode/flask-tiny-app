if [ ! -d "env" ]; then
    echo "Tạo virtual environment..."
    python3 -m venv env
fi

echo "Kích hoạt virtual environment..."
source env/bin/activate

echo "Nâng cấp pip..."
pip install --upgrade pip

# Bước 4: Cài đặt các dependencies từ requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Cài đặt dependencies từ requirements.txt..."
    pip install -r requirements.txt
else
    echo "Không tìm thấy file requirements.txt. Kiểm tra lại."
    exit 1
fi

echo "Tạo migration..."
python manage.py makemigrations

echo "Áp dụng migration..."
python manage.py migrate

if python manage.py help | grep -q "populate_blog"; then
    echo "Đang tạo dữ liệu mẫu..."
    python manage.py populate_blog
fi

echo "Để tạo superuser, hãy chạy: python manage.py createsuperuser"

echo "Khởi chạy development server..."
python manage.py runserver