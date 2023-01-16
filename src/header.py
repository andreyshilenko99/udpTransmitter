from struct import pack


MARKER = int("EEEE", 16)


class Header:
    def __init__(self, message_number: int, size_block_data: int) -> None:
        self.header = pack('>HIH', MARKER, message_number, size_block_data)
