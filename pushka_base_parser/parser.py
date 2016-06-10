import abc
import json
import os


class Parser(object):
    __metaclass__ = abc.ABCMeta

    SOURCE_ID = None

    def __init__(self, store_factory):
        self._client = None

        if self.SOURCE_ID is None:
            raise ValueError('SOURCE_ID should not be None')

        self._store_factory = store_factory

    def handle(self, message, client):
        self._client = client
        store = self._store_factory(message['id'])
        result = self.parse(message, store, client)
        store.close()
        return result

    def send(self, alert):
        if self._client is None:
            raise ValueError('Calling `send` only allowed in parse method')

        self._client.send(json.dumps(alert))

    @abc.abstractmethod
    def parse(self, subscription, store, client):
        pass

    def get_list(self, list_id, query):
        pass

    def get_context(self, params):
        pass

    @staticmethod
    def get_param(key, default=None):
        os.getenv(key, default)
