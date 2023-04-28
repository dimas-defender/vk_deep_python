import socket
import threading
from queue import Queue
from sys import argv


class Client:
    def __init__(self, urls, n_threads=10):
        self.urls = urls
        self.n_threads = n_threads
        self.url_queue = Queue()

        self.threads = [
            threading.Thread(
                target=self.send_request,
                args=[i]
            )
            for i in range(self.n_threads)
        ]

        for thread in self.threads:
            thread.start()

    def fill_queue(self):
        for url in self.urls:
            self.url_queue.put(url[:len(url)-1])

        self.url_queue.put('EOF')

        for thread in self.threads:
            thread.join()

    def send_request(self, tid):
        while True:
            url = self.url_queue.get()
            if url == 'EOF':
                self.url_queue.put('EOF')
                break

            try:
                client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_sock.connect(("localhost", 15000))
                client_sock.sendall(url.encode())
                data = client_sock.recv(4096)
                print(url + ": " + data.decode())
                client_sock.close()

            except Exception as e:
                print(f'ERROR in thread{tid}: {e}')


if __name__ == '__main__':
    with open(argv[2], "r") as urls_file:
        client = Client(urls_file, int(argv[1]))
        client.fill_queue()
