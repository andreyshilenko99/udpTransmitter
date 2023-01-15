import json
import time

from client.client import Client
from utils import from_json_to_list
from message.message import Message
from header.header import Header
from block_data.block_data import BlockData
from utils import get_config


def start_client(file_name: str, path_to_config: str):
    config = get_config(path_to_config)['client']
    client = Client(config['host'], config['port'])
    try:
        client.connect()
        message_number = 0
        list_jsons = from_json_to_list(file_name)
        for counter in range(0, len(list_jsons)):
            param_pairs_list = [{pair: list_jsons[counter][pair]} for pair in list_jsons[counter]]
            for pair_number in range(0, len(param_pairs_list)):
                param_pair = param_pairs_list[pair_number]
                block_data = BlockData(counter, len(list_jsons[counter].keys()), pair_number,
                                       json.dumps(param_pair))
                header = Header(message_number, len(block_data.block_data))
                msg = Message(header, block_data)
                client.send_msg(msg.message)
                message_number += 1
                time.sleep(1)
        client.close_connection()
    except ConnectionRefusedError:
        client.close_connection()


if __name__ == '__main__':
    start_client('../data/dump.json', '../config/config.yaml')
