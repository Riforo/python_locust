from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    # Модель настроек с дефолтными значениями
    base_url: str = Field("https://dev-api.example.com", validation_alias="BASE_URL")
    
    # Настройка для чтения из .env файла
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

# Создаем один экземпляр (синглтон)
config = Settings()