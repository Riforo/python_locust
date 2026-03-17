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