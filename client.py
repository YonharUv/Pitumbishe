import socket
import threading
import os

class Client:

    UDP_MAX_SIZE = 65535

    def __init__(self, host: str = '127.0.0.1', port: int = 3000):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.s.connect((host, port))
        self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


    def listen(s: socket.socket):
        while True:
            msg = s.recv(Client.UDP_MAX_SIZE)
            print('\r\r' + msg.decode('utf-8') + '\n' + f'you: ', end='')

    def connect(self):   
        threading.Thread(target=Client.listen, args=(self.s,), daemon=True)
        self.s.send('__join'.encode('utf-8'))
        while True:
            msg = input(f'you: ')
            self.s.send(msg.encode('utf-8'))
            if msg == 'close':
                exit()
 


if __name__ == '__main__':
    os.system('cls')
    print('Welcome to chat!')
    client = Client()
    client.connect()

