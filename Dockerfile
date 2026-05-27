# Base image
FROM python:3.10-slim

# Working directory set karo
WORKDIR /app

# Requirements copy karo
COPY requirements.txt .

# Dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# Saari files copy karo
COPY . .

# Port open karo
EXPOSE 8000

# API start karo
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]