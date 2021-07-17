import requests
import hashlib
import json
import base64
import time
import hmac
from config import SECRET_KEY, API_URL


class CoinoneReq:
    def __get_encoded_payload(self, payload: dict):
        payload['nonce'] = int(time.time() * 1000)

        dumped_json = json.dumps(payload)
        encoded_json = base64.b64encode(bytes(dumped_json, 'utf-8'))
        return encoded_json

    def __get_signature(self, encoded_payload):
        signature = hmac.new(bytes(SECRET_KEY, 'utf-8'), encoded_payload, hashlib.sha512)
        return signature.hexdigest()

    def post(self, action: str, payload: dict):
        url = '{}/{}'.format(API_URL, action)

        encoded_payload = self.__get_encoded_payload(payload)

        headers = {
            'Content-type': 'application/json',
            'X-COINONE-PAYLOAD': encoded_payload,
            'X-COINONE-SIGNATURE': self.__get_signature(encoded_payload),
        }

        response = requests.post(url, headers=headers, data=encoded_payload)

        return json.loads(response.content)
