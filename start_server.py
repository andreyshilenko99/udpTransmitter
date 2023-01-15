from server.server import Server
from utils import get_config


def start_server(path_to_config: str):
    config = get_config(path_to_config)['server']
    server = Server(config['conn_number'], config['host'], config['port'])
    server.run()


if __name__ == '__main__':
    start_server('../config/config.yaml')