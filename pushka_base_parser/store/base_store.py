class Store(object):
    def __init__(self, subscription_id):
        self._subscription_id = subscription_id

    def set_state(self, state):
        pass

    def set_value(self, key, value):
        pass

    def push_all(self, key, values):
        pass

    def get_value(self, key, default=None):
        pass

    def get_state(self):
        pass

    def close(self):
        pass
