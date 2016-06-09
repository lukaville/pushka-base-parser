import abc
import os


class Parser(object):
    __metaclass__ = abc.ABCMeta

    SOURCE_ID = None

    def __init__(self, store_factory):
        if self.SOURCE_ID is None:
            raise ValueError('SOURCE_ID should not be None')

        self._store_factory = store_factory

    def handle(self, message, client):
        store = self._store_factory(message['id'])
        result = self.parse(message, store, client)
        store.close()
        return result

    @abc.abstractmethod
    def parse(self, subscription, store, client):
        pass

    @staticmethod
    def get_param(key, default=None):
        os.getenv(key, default)
