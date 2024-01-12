# echo-server.py

import socket
from json import loads
from threading import Thread
from threading import Event
from requests import post
import requests

class hardware_server:
    def __init__(self, host: str = "127.0.0.1", port: int = 65432):
        # Port to listen on (non-privileged ports are > 1023)
        self.__mainURL = 'http://localhost:8000/api/send/'
        self.__hardwares_info = {}
        self.__threads = {}
        self.__start_socket(host, port)

    def __handle_client(self, event, client_sock, addr):
        print(client_sock, addr)
        with client_sock:
            while True:
                data = client_sock.recv(1024)
                if not data:
                    break
                if event.is_set():
                    break
                cli_hwr_info = loads(data.decode('utf-8'))
                [cli_hwr_info[key].update({"ip_client": addr[0]}) for key in cli_hwr_info.keys()]
                self.__hardwares_info.update(cli_hwr_info)
                try:
                    post(self.__mainURL, json=cli_hwr_info)
                except requests.exceptions.ConnectionError:
                    print("Error while send POST to server!, server API is offline ?")
                    continue
            self.__threads.pop(addr)

    def __start_socket(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen()
            event = Event()
            while True:
                try:
                    conn, addr = s.accept()
                    self.__threads[addr] = Thread(target=self.__handle_client, args=(event, conn, addr))
                    self.__threads[addr].start()
                except KeyboardInterrupt:
                    event.set()
                    break
        print("\nClosing server!")

    def __del__(self):
        print("Finish!")

hardware_server()
