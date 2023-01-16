import json
from struct import unpack

from src.header import Header
from src.block_data import BlockData


class Message:
    def __init__(self, header: Header, block_data: BlockData):
        if len(header.header) == 8 and len(block_data.block_data) == 8 + block_data.json_str_length:
            self.message = header.header + block_data.block_data
        else:
            raise Exception(ValueError)

    @staticmethod
    def deserialization(message: bytes) -> dict:
        header = unpack('>HIH', message[:8])
        block_data_info = unpack('>HHHH', message[8:16])
        data = json.loads(message[16:])
        deserialized_msg = {'header':
                                {'marker': hex(header[0]),
                                 'msg_number': header[1],
                                 'block_data_size': header[2]},
                            'block_data':
                                {'json_id': block_data_info[0],
                                 'json_strs_total': block_data_info[1],
                                 'json_str_number': block_data_info[2],
                                 'json_str_length': block_data_info[3],
                                 'json_str': data}}
        return deserialized_msg
