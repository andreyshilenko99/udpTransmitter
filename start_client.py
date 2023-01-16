import json
import time

from src.client import Client
from src.utils import from_json_to_list
from src.message import Message
from src.header import Header
from src.block_data import BlockData
from src.utils import get_config


def start_client(file_name: str, path_to_config: str) -> None:
    config = get_config(path_to_config)['client']
    client = Client(config['host'], config['port'])
    try:
        client.connect()
        list_jsons = from_json_to_list(file_name)
        message_number = 1
        pair_number = 0
        id = 1
        for message in list_jsons:
            param_pairs_list = [{pair: message[pair]} for pair in message]
            for pair_param in param_pairs_list:
                pair_number += 1
                block_data = BlockData(id, len(message.keys()), pair_number,
                                       json.dumps(pair_param))
                header = Header(message_number, len(block_data.block_data))
                msg = Message(header, block_data)
                client.send_msg(msg.message)
                message_number += 1
                time.sleep(0.5)
            pair_number = 0
            id += 1

        client.close_connection()
    except ConnectionRefusedError:
        client.close_connection()


if __name__ == '__main__':
    start_client('data/dump.json', './config.yaml')
