import json
import socket
import time
from message.message import Message
from struct import unpack


class Server:

    def __init__(self, connections: int, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen(connections)

    def run(self):
        global packets
        try:
            conn, addr = self.sock.accept()
            print('connected:', addr)
            packets = []
            while True:
                data = conn.recv(1024)
                packet = Message.deserialization(data)
                print(f"Packet №{packet['header']['msg_number']} received!")
                packets.append(packet)
                conn.send(data.upper())
                time.sleep(1)
        except ConnectionResetError:
            for pack in packets:
                
