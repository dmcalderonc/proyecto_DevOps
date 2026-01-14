# Usamos Python
FROM python:3.11-slim

# Directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . .

# Puerto por defecto de Django
EXPOSE 8000

# Comando para correr el servidor de Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]