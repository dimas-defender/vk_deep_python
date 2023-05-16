import socket
import threading
import argparse
from queue import Queue
from collections import Counter
from json import dumps
from re import findall
from requests import get
from bs4 import BeautifulSoup


def handle_url(url, n_words):
    html = get(url).text
    text = BeautifulSoup(html, features='html.parser').text
    cleared_text = findall(r'[а-яёА-ЯЁa-zA-Z]+', text)
    counter = Counter(cleared_text)
    top_words = dict(counter.most_common(n_words))
    return dumps(top_words, ensure_ascii=False)


class Server:
    def __init__(self, n_workers=10, n_words=7, url_handler=handle_url):
        self.n_workers = n_workers
        self.n_words = n_words
        self.url_handler = url_handler
        self.url_queue = Queue(100)
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
            for i in range(self.n_workers)
        ]

        for thread in threads:
            thread.start()

        while True:
            client_sock, _ = self.server_sock.accept()
            self.url_queue.put(client_sock)

            if not client_sock:
                break

        for thread in threads:
            thread.join()

    def handle_request(self, tid):
        while True:
            try:
                client_sock = self.url_queue.get()

                if client_sock is None:
                    self.url_queue.put(None)
                    break

                data = client_sock.recv(4096)
                if not data:
                    self.url_queue.put(None)
                    break

                response = self.url_handler(data.decode(), self.n_words)
                client_sock.sendall(response.encode())
                client_sock.close()

                with self.lock:
                    self.urls_handled += 1
                    print(f'Thread {tid}: {self.urls_handled} urls handled')

            except Exception as e:
                print(f'ERROR in thread{tid}: {e}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-w", type=int)
    parser.add_argument("-k", type=int)
    args = parser.parse_args()

    server = Server(args.w, args.k)
    server.start()
