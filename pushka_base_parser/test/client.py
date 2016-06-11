import json


class TestClient:
    def __init__(self, callback):
        self._callback = callback

    def send(self, message):
        self._callback(json.loads(message))
