from fastapi import APIRouter, Response
from app.services.markets import get_market_price_cur
from app.providers.res_helper import response_success, response_failure

market_router = APIRouter()


@market_router.get("/prices/{currency}")
def get_market_price(currency: str, response: Response):
    try:
        return response_success(get_market_price_cur(currency))
    except Exception as e:
        response_failure(response, e)
