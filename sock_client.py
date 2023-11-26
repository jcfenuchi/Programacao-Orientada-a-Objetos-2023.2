
from time import sleep
from wandl import Monitoring
import json
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class Agent_mon(Monitoring):
    def __init__(self, host: str = "127.0.0.1", port: int = 65432):
        self.__try_con(host, port)

    def __try_con(self, host, port):
        try_time = 0
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    while True:
                        try:
                            s.connect((host, port))
                            try_time = 0
                            while True:
                                self.__send_hwr_info(s)
                        except Exception:
                            break
                sleep(60)
                try_time += 1
                print(f"Try Connect to {host}:{port} - try:{try_time}")
            except KeyboardInterrupt:
                break

    def __send_hwr_info(self, sock):
        sock.sendall(json.dumps({socket.gethostname():self.get_system_info()}).encode('utf-8'))
        sleep(5)

    def __del__(self):
        print("Finish!")

Agent_mon()
