# Sử dụng image chứa Python
FROM python:3.11.7-alpine3.19

# Thiết lập thư mục làm việc
WORKDIR /app

# Sao chép tất cả các file trong thư mục hiện tại vào thư mục /app trong container
COPY . .

# Cài đặt các dependencies từ requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose cổng 8501 để truy cập ứng dụng Streamlit
EXPOSE 8501

# Khởi chạy ứng dụng Streamlit
CMD ["streamlit", "run", "app.py"]
