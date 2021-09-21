from pydantic import BaseSettings


class Settings(BaseSettings):
    API_V1 = "/app/v1"
    PROJECT_NAME = "Coinone Trading Provider"


settings = Settings()
