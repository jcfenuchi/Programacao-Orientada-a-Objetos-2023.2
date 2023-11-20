# echo-server.py

import socket
from json import loads
from threading import Thread


class hardware_server:
    def __init__(self, host: str = "127.0.0.1", port: int = 65432):
        # Port to listen on (non-privileged ports are > 1023)
        self.__start_socket(host, port)
        self.__hardwares_info = {}

    def __handle_client(self, client_sock, addr):
        with client_sock:
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                cli_hwr_info = loads(data.decode('utf-8'))
                [cli_hwr_info[key].update({"ip_client": addr[0]}) for key in cli_hwr_info.keys()]
                self.__hardwares_info.update(cli_hwr_info)

    def __start_socket(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            while True:
                conn, addr = s.accept()
                th = Thread(target=self.__handle_client, args=(conn, addr))
                th.start()
