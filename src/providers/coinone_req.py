import requests
import hashlib
import json
import base64
import time
import hmac
from config import ACCESS_TOKEN
from datetime import datetime
from config import SECRET_KEY, API_URL


class CoinoneReq:
    def _get_encoded_payload(self, payload: dict):
        payload['nonce'] = int(time.time() * 1000)

        dumped_json = json.dumps(payload)
        encoded_json = base64.b64encode(bytes(dumped_json, 'utf-8'))
        return encoded_json

    def _get_signature(self, encoded_payload: bytes):
        signature = hmac.new(bytes(SECRET_KEY, 'utf-8'), encoded_payload, hashlib.sha512)
        return signature.hexdigest()

    def _get_headers(self, encoded_payload: bytes):
        return {
            'Content-type': 'application/json',
            'X-COINONE-PAYLOAD': encoded_payload,
            'X-COINONE-SIGNATURE': self._get_signature(encoded_payload),
        }

    def generate_nonce(self):
        return datetime.datetime.now().timestamp()

    def post(self, action: str, payload={}):
        url = '{}/{}'.format(API_URL, action)
        payload['access_token'] = ACCESS_TOKEN

        encoded_payload = self._get_encoded_payload(payload)
        headers = self._get_headers(encoded_payload)

        response = requests.post(url, headers=headers, data=encoded_payload)

        return json.loads(response.content)
