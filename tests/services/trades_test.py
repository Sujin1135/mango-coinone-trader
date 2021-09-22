from app.services.trades import sell, buy, cancel_buy, cancel_sell


def test_sell():
    sut = sell(35000000, 0.001, "BTC")

    assert len(sut["result"]) > 0


def test_sell_eth_little():
    sut = sell(4051000, 0.0015, "ETH")

    assert sut["result"] == "success"


# TODO: 바로 매도가 되지 않을만한 가격을 얻어서 매도 요청을 하도록 수정
def test_cancel_sell():
    price = 3700000
    qty = 0.0015
    currency = "ETH"
    result = sell(price, qty, currency)
    order_id = result["orderId"]

    sut = cancel_sell(order_id, price, qty, currency)
    assert sut["result"] == "success"


# TODO: 바로 매수가 되지 않을만한 가격을 얻어서 매수 요청을 하도록 수정
def test_cancel_buy():
    price = 2000000
    qty = 0.005
    currency = "ETH"
    result = buy(price, qty, currency)
    order_id = result["orderId"]

    sut = cancel_buy(order_id, price, qty, currency)
    assert sut["result"] == "success"
