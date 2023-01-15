import socket
from message.message import Message


class Client:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.host = host

    def connect(self):
        self.sock.connect((self.host, self.port))

    def send_msg(self, message: bytes):
        self.sock.send(message)

    def receive(self):
        data = self.sock.recv(1024)
        print(data)

    def close_connection(self):
        self.sock.close()
