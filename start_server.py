from server.server import Server
from utils import get_config


def start_server():
    config = get_config('../config/config.yaml')['server']
    server = Server(config['conn_number'], config['host'], config['port'])
    server.run()


if __name__ == '__main__':
    start_server()