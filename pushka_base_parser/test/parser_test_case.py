import json
import unittest

from pushka_base_parser import MemoryStore
from pushka_base_parser.test.client import TestClient


def parse(parser, params, sub_id='abc', multiple_send=False):
    subscription = {
        'id': sub_id,
        'params': params
    }

    messages = []
    parser.handle(json.dumps(subscription),
                  TestClient(lambda msg: messages.append(msg)))

    if len(messages) == 0:
        return None

    return messages if multiple_send else messages[0]


class ParserTestCase(unittest.TestCase):
    def setUp(self):
        self._store = MemoryStore()

    @property
    def store_factory(self):
        return lambda sub_id: self._store

    @property
    def state(self):
        return self._store.get_state()

    @state.setter
    def state(self, state):
        self._store.set_state(state)
