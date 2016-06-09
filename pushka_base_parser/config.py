import os


def get_config(source_id):
    config = {
        'RABBIT_PORT': 5672,
        'RABBIT_OUTPUT_ROUTING_KEY': 'push_router',
        'RABBIT_OUTPUT_EXCHANGE_TYPE': 'direct',
        'RABBIT_OUTPUT_EXCHANGE': 'alerts',
        'RABBIT_INPUT_ROUTING_KEY': source_id,
        'RABBIT_INPUT_QUEUE_NAME': source_id,
        'RABBIT_INPUT_EXCHANGE_TYPE': 'direct',
        'RABBIT_INPUT_EXCHANGE': 'source_handlers',
        'RABBIT_HOST': 'ampq',
        'MONGO_PORT': 27017,
        'MONGO_HOST': 'db',
        'MONGO_DATABASE': 'pushka',
        'MONGO_COLLECTION': 'states'
    }

    for k, v in config.items():
        config[k] = os.getenv(k, v)

    return config
