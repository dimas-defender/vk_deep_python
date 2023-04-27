import socket
import threading
import queue
import sys
from collections import Counter
import json
import re
import requests
from bs4 import BeautifulSoup


class Server:
    def __init__(self, N_workers=10, N_words=7):
        self.N_workers = N_workers
        self.N_words = N_words
        self.url_queue = queue.Queue()
        self.lock = threading.Lock()
        self.urls_handled = 0

        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_sock.bind(("localhost", 15000))
        self.server_sock.listen()

    def start(self):
        threads = [
            threading.Thread(
                target=self.handle_request,
                args=[i]
            )
            for i in range(self.N_workers)
        ]

        for th in threads:
            th.start()

        while True:
            client_sock, _ = self.server_sock.accept()
            self.url_queue.put(client_sock)

            if not client_sock:
                break

        for th in threads:
            th.join()

    def handle_request(self, tid):
        while True:
            client_sock = self.url_queue.get()

            if client_sock is None:
                self.url_queue.put(None)
                break

            data = client_sock.recv(4096)
            if not data:
                self.url_queue.put(None)
                break

            try:
                text_data = requests.get(data.decode()).text
                text = BeautifulSoup(text_data, features='html.parser').text
                cleared_text = re.findall(r'[а-яёА-ЯЁa-zA-Z]+', text)
                counter = Counter(cleared_text)
                top_words = dict(counter.most_common(self.N_words))
                response = json.dumps(top_words, ensure_ascii=False)

                client_sock.sendall(response.encode())
                client_sock.close()

                with self.lock:
                    self.urls_handled += 1
                    print(f'Thread {tid}: {self.urls_handled} urls handled')

            except Exception as e:
                print(f'ERROR in thread{tid}: {e}')


if __name__ == '__main__':
    server = Server(int(sys.argv[1]), int(sys.argv[2]))
    server.start()
