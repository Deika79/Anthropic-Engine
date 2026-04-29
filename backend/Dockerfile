FROM python:3.11-slim

WORKDIR /app

# instalar dependencias del sistema (mínimas)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# copiar requirements
COPY requirements.txt .

# instalar dependencias python
RUN pip install --no-cache-dir -r requirements.txt

# copiar app
COPY app ./app

# exponer puerto
EXPOSE 10000

# comando arranque
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]