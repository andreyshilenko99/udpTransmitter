from struct import pack


class BlockData:
    def __init__(self,
                 json_id: int,
                 json_strs_total: int,
                 json_str_number: int,
                 json_str: str) -> None:
        self.json_str_length = len(json_str)
        data = [json_id, json_strs_total,
                json_str_number, self.json_str_length]
        self.block_data = pack('>{}H'.format(len(data)), *data) + pack(f"{self.json_str_length}s", bytes(json_str, 'UTF-8'))
