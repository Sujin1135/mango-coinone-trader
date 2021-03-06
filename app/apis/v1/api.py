from fastapi import APIRouter
from app.apis.v1.endpoints.accounts import account_router
from app.apis.v1.endpoints.markets import market_router
from app.apis.v1.endpoints.trades import trade_router

api_router = APIRouter()


@api_router.get("/health-check")
def health_check():
    return {"result": True}


api_router.include_router(account_router, prefix="/accounts", tags=["accounts"])
api_router.include_router(market_router, prefix="/markets", tags=["markets"])
api_router.include_router(trade_router, prefix="/trades", tags=["trades"])
