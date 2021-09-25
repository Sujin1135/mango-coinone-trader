from fastapi import APIRouter
from app.services.markets import get_market_price_cur

router = APIRouter()


@router.get("/prices")
def get_market_price(currency: str):
    return {"data": get_market_price_cur(currency)}
