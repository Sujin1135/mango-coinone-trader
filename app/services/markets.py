from app.providers.coinone_req import CoinoneReq

req = CoinoneReq()


def get_market_price_cur(currency: str):
    return req.get(action="ticker?currency={}".format(currency))
