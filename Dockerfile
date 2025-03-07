
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations && python manage.py migrate

EXPOSE 8000

# Command chạy ứng dụng
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]