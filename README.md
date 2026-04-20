# Locust Performance Testing Framework

Фреймворк для нагрузочного тестирования на базе **Python** и **Locust**. 
Проект построен по модульной схеме: разделение на сценарии, сервисы и профили нагрузки.

## 🚀 Структура проекта

*   `profile/` — описание типов пользователей (User), их веса и базовые настройки.
*   `task/` — наборы задач (TaskSet) и бизнес-логика сценариев.
*   `api/service/` — описание API-клиентов (Service Layer) для взаимодействия с эндпоинтами.
*   `api/models/` — Pydantic-модели для валидации ответов API.

## 🛠 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com
   cd python_locust

2. Создайте и активируйте виртуальное окружение
    ```python -m venv .venv
    source .venv/bin/activate  # Для Linux/macOS
    .venv\Scripts\activate     # Для Windows

3. Установите зависимости
    ```
    pip install -r requirements.txt

## 🏃 Запуск тестов

Для запуска проекта убедитесь, что виртуальное окружение активировано и зависимости установлены (`pip install -r requirements.txt`).

### 1. Запуск с графическим интерфейсом (Web UI)
После запуска откройте в браузере [http://localhost:8089](http://localhost:8089):
```bash
# Запуск всех доступных профилей
locust -f profile/test_profile.py

# Запуск конкретного профиля (например, BaseUserWithServiser)
locust -f profile/test_profile.py BaseUserWithServiser
```

### 2. Консольный запуск (Headless)
Используется для автоматизации и CI/CD:

```
locust -f profile/test_profile.py --headless -u 100 -r 10 --run-time 5m --host https://jsonplaceholder.typicode.com
```
-u 100: количество виртуальных пользователей.\
-r 10: скорость появления (users per second).\
--run-time 5m: длительность теста 5 минут..

## 🐳 Запуск в Docker
Проект полностью контейнеризирован и готов к работе в распределенном режиме (Master-Worker).

### Запуск локального кластера:
```bash
# Сборка и запуск Master и Worker (по умолчанию 1 воркер)
docker-compose up --build 
```
### Масштабирование нагрузки:
Если одного воркера недостаточно для генерации нагрузки, увеличьте их количество:
```bash
# Запуск 4-х воркеров параллельно
docker-compose up --scale worker=4 -d
```
### Остановка проекта
```bash
docker-compose down
