FROM python:3.11-slim

WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código
COPY . .

# Crear directorio para la base de datos
RUN mkdir -p /app/data

# Variables de entorno
ENV PYTHONUNBUFFERED=1

# Comando para ejecutar el bot
CMD ["python", "main.py"]