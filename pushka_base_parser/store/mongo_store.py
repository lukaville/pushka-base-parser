from pymongo import MongoClient

from parser.store.base_store import Store


class MongoStore(Store):
    def __init__(self, subscription_id, config):
        super().__init__(subscription_id)

        self._client = MongoClient(config['MONGODB_HOST'],
                                   config['MONGO_PORT'])

        self._db = self._client.get_database(config['MONGO_DATABASE'])
        self._collection = self._db[config['MONGO_COLLECTION']]

    def set_state(self, state):
        self._collection.replace_one({'_id': self._subscription_id}, state, upsert=True)

    def set_value(self, key, value):
        self._collection.update_one({'_id': self._subscription_id}, {'$set': {key: value}}, upsert=True)

    def push_all(self, key, values):
        self._collection.update_one({'_id': self._subscription_id}, {'$push': {key: {'$each': values}}}, upsert=True)

    def get_value(self, key, default=None):
        state = self.get_state()
        if state:
            return state.get(key, default)
        return default

    def get_state(self):
        return self._collection.find_one({'_id': self._subscription_id})

    def get_collection(self):
        return self._collection

    def close(self):
        self._client.close()
