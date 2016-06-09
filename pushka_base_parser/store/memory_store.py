from pushka_base_parser.store.base_store import Store


class MemoryStore(Store):
    def __init__(self, subscription_id):
        super().__init__(subscription_id)
        self._state = {}

    def set_state(self, state):
        self._state = state

    def set_value(self, key, value):
        self._state[key] = value

    def push_all(self, key, values):
        if key not in self._state:
            self._state[key] = []

        if type(self._state[key]) != list:
            raise TypeError('Object `{key}` should be a list'.format(key=key))

        self._state[key].extend(values)

    def get_value(self, key, default=None):
        return self._state.get(key, default)

    def get_state(self):
        return self._state

    def close(self):
        pass
