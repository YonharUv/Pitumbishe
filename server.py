import socket

class Server:
    UDP_MAX_SIZE = 65535
    def __init__(self, host: str = '127.0.0.1', port: int = 3000) -> None:
        self.serv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.serv.bind((host, port))
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print(f'Listening at {host}:{port}')

    def mainloop(self) -> None:
        members = []
        while True:
            
            msg, addr = self.serv.recvfrom(Server.UDP_MAX_SIZE)

            if addr not in members:
                members.append(addr)
            
            if not msg:
                continue

            client_id = addr[1]
            if msg.decode('utf-8') == '__join':
                print(f'Client {client_id} joined chat')


            elif msg.decode('utf-8') == 'close':
                print(f'Client {client_id} lefted chat')


            msg = f'client{client_id}: {msg.decode("utf-8")}'
            for member in members:
                if member == addr:
                    continue

                self.serv.sendto(msg.encode('utf-8'), member)


if __name__ == '__main__':
    server = Server()
    server.mainloop()
