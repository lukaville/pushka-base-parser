from rabbit_bind import RabbitBinder


class Runner(object):
    def __init__(self, parser, config):
        self._parser = parser
        self._config = config
        self._binder = RabbitBinder(
            host=self._config['RABBIT_HOST'],
            connection_attempts=10,
            retry_delay=10,
            requeue=False
        )

    def run(self):
        self._binder.bind(
            input_exchange=self._config['RABBIT_INPUT_EXCHANGE'],
            input_exchange_type=self._config['RABBIT_INPUT_EXCHANGE_TYPE'],
            input_queue_name=self._config['RABBIT_INPUT_QUEUE_NAME'],
            input_routing_key=self._config['RABBIT_INPUT_ROUTING_KEY'],
            output_exchange=self._config['RABBIT_OUTPUT_EXCHANGE'],
            output_exchange_type=self._config['RABBIT_OUTPUT_EXCHANGE_TYPE'],
            output_routing_key=self._config['RABBIT_OUTPUT_ROUTING_KEY'],
            handler=self._parser.handler
        )
        self._binder.start()
        self._binder.close()
