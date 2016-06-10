from multiprocessing import Process

from rabbit_bind import RabbitBinder
from rabbit_rpc import RabbitRpcServer


class Runner(object):
    def __init__(self, parser, config, rpc=False):
        self._parser = parser
        self._config = config
        self._start_rpc = rpc
        self._binder = RabbitBinder(
            host=self._config['RABBIT_HOST'],
            connection_attempts=10,
            retry_delay=10,
            requeue=False
        )

        if rpc:
            self._rabbit_rpc_server = RabbitRpcServer(
                host=config['RABBIT_HOST'],
                exchange=config['RABBIT_RPC_EXCHANGE'],
                routing_key=config['RABBIT_RPC_ROUTING_KEY']
            )
            self._rabbit_rpc_server.add_callback(self._parser.get_list)
            self._rabbit_rpc_server.add_callback(self._parser.get_context)

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

        print('Starting parser...')
        Process(target=self._binder.start).start()

        if self._start_rpc:
            print('Starting RPC server...')
            Process(target=self._rabbit_rpc_server.start).start()

        self._binder.close()
