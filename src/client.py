import socket


class Client:
    def __init__(self, host: str, port: int) -> None:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.port = port
        self.host = host

    def connect(self) -> None:
        self.sock.connect((self.host, self.port))

    def send_msg(self, message: bytes) -> None:
        self.sock.send(message)

    def receive(self) -> None:
        data = self.sock.recv(1024)
        print(data)

    def close_connection(self) -> None:
        self.sock.close()
