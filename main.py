from fastapi import FastAPI
from app.core.config import settings
from app.apis.v1.api import router

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(router, prefix=settings.API_V1)
