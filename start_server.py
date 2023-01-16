from src.server import Server
from src.utils import get_config


def start_server(path_to_config: str) -> None:
    config = get_config(path_to_config)['server']
    server = Server(config['conn_number'], config['host'], config['port'])
    server.run()


if __name__ == '__main__':
    start_server('./config.yaml')