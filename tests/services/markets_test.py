import pytest

from app.services.markets import get_market_price_cur


@pytest.mark.parametrize("currency", ["BTC", "ETH", "XRP"])
def test_get_market_currency_price_currently(currency: str):
    sut = get_market_price_cur(currency)

    assert sut["result"] == "success"
