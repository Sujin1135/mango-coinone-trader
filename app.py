from flask import Flask
from config import ACCESS_TOKEN
from src.providers.coinone_req import CoinoneReq


app = Flask(__name__)


@app.route('/')
def hello_world():
    payload = {"access_token": ACCESS_TOKEN}

    req = CoinoneReq()

    return req.get_post_response(action='v2/account/balance', payload=payload)


if __name__ == '__main__':
    app.run()
