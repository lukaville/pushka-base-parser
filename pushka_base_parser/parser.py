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
        subscription = json.loads(message)
        self._client = client
        store = self._store_factory(subscription['id'])
        result = self.parse(subscription, store)
        store.close()
        return result

    def send(self, alert):
        if self._client is None:
            raise ValueError('Calling `send` only allowed in parse method')

        self._client.send(json.dumps(alert))

    @abc.abstractmethod
    def parse(self, subscription, store):
        pass

    def get_list(self, list_id, query):
        pass

    def get_details(self, **kwargs):
        pass

    @staticmethod
    def get_param(key, default=None):
        os.getenv(key, default)
