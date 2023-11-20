
from time import sleep
from wandl import Monitoring
import json
import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

class Agent_mon(Monitoring):
    def __init(self, host: str = "127.0.0.1", port: int = 65432):
        self.__try_con(host, port)

    def __try_con(self, host, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try_time = 0
            timeout_con = 60
            while True:
                try:
                    s.connect((host, port))
                except Exception:
                    try_time += 1
                    print(f"error try time {try_time}")
                    sleep(timeout_con)
                    continue
                break
            self.__send_hwr_info(s)

    def __send_hwr_info(self, sock):
        while True:
            try:
                sock.sendall(json.dumps({socket.gethostname():self.get_system_info()}).encode('utf-8'))
                sleep(60)
            except KeyboardInterrupt:
                break
            except Exception as ex:
                print(f"error {ex}")