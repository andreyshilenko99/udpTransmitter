import json
import socket
import time
from src.message import Message


class Server:

    def __init__(self, connections: int, host: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(connections)

    def run(self) -> None:
        packets = {}
        try:
            conn, addr = self.sock.accept()
            print('connected:', addr)
            while True:
                data = conn.recv(1024)
                packet = Message.deserialization(data)
                print(f"Packet №{packet['header']['msg_number']} received!")
                print(json.dumps(packet, indent=3))
                if packet['block_data']['json_id'] not in packets:
                    packets[packet['block_data']['json_id']] = []
                    packets[packet['block_data']['json_id']].append(packet['block_data'])
                else:
                    packets[packet['block_data']['json_id']].append(packet['block_data'])
                conn.send(data.upper())
        except ConnectionResetError:
            for i in packets.keys():
                msg = {}
                for j in packets[i]:
                    if j['json_str_number']:
                        msg.update(j['json_str'])
                print(f"JSON №{i}")
                print(json.dumps(msg, indent=3))
