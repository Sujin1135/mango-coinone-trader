from fastapi import APIRouter
from app.apis.v1.endpoints.accounts import account_router

api_router = APIRouter()


@api_router.get("/health-check")
def health_check():
    return {"result": True}


api_router.include_router(account_router, prefix="/accounts", tags=["accounts"])
