# Используем официальный образ Python
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем зависимости
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта в контейнер
COPY . /app/

# Открываем порт, на котором будет работать Django
EXPOSE 8000

# Команда для запуска сервера Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
