from struct import pack


class BlockData:
    __slots__ = ['block_data']

    def __init__(self, json_id: int, json_strs_total: int,
                 json_str_number: int, json_str: str):
        json_str_length = len(json_str)
        data = [json_id, json_strs_total,
                json_str_number, json_str_length]

        self.block_data = pack('>{}H'.format(len(data)), *data) + pack(f"{json_str_length}s", bytes(json_str, 'UTF-8'))





