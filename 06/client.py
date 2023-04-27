import socket
import threading
import queue
import sys


class Client:
    def __init__(self, urls, N_threads=10):
        self.urls = urls
        self.N_threads = N_threads
        self.url_queue = queue.Queue()

        self.threads = [
            threading.Thread(
                target=self.send_request,
                args=[i]
            )
            for i in range(self.N_threads)
        ]

        for th in self.threads:
            th.start()

    def fill_queue(self):
        for url in self.urls:
            self.url_queue.put(url[:len(url)-1])

        self.url_queue.put('EOF')

        for th in self.threads:
            th.join()

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
    with open(sys.argv[2], "r") as urls_file:
        client = Client(urls_file, int(sys.argv[1]))
        client.fill_queue()
