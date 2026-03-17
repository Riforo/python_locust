FROM python:3.11-slim

# Настройка рабочего каталога
WORKDIR /mnt/locust

# Установка зависимостей
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект (profile, task, service и т.д.)
COPY . .

# Порты для Web UI и связи Master-Worker
EXPOSE 8089 5557