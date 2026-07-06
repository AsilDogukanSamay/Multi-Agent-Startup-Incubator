import os
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    gemini_api_key: str = ""
    port: int = 8000
    host: str = "127.0.0.1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

# Instantiate settings
try:
    settings = Settings()
except Exception:
    # Fallback if .env is missing or has parsing errors during initial setup
    class FallbackSettings:
        gemini_api_key = os.getenv("GEMINI_API_KEY", "")
        port = int(os.getenv("PORT", "8000"))
        host = os.getenv("HOST", "127.0.0.1")
    settings = FallbackSettings()
