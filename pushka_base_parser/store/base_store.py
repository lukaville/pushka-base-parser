import abc


class Store(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, subscription_id):
        self._subscription_id = subscription_id

    @abc.abstractmethod
    def set_state(self, state):
        pass

    @abc.abstractmethod
    def set_value(self, key, value):
        pass

    @abc.abstractmethod
    def push_all(self, key, values):
        pass

    @abc.abstractmethod
    def get_value(self, key, default=None):
        pass

    @abc.abstractmethod
    def get_state(self):
        pass

    @abc.abstractmethod
    def close(self):
        pass
