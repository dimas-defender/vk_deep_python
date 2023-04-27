from unittest import TestCase, mock
from server import Server


class TestServer(TestCase):
    @mock.patch('socket.socket')
    def test_handle_request(self, server_mock):
        client_mock = mock.Mock()
        client_mock.recv.side_effect = [
            'https://vk.com'.encode(),
            'https://google.com'.encode(),
            'https://yandex.com'.encode()
        ]

        server_mock.return_value = server_mock
        server_mock.accept.side_effect = [
            (client_mock, None),
            (client_mock, None),
            (client_mock, None),
            (None, None)
        ]

        server = Server()
        server.start()

        self.assertEqual(4, server_mock.accept.call_count)
        self.assertEqual(3, client_mock.recv.call_count)
        self.assertEqual(3, server.urls_handled)

    @mock.patch("socket.socket")
    @mock.patch("threading.Thread")
    def test_create_threads(self, thread_mock, server_mock):
        thread_mock.return_value = thread_mock
        server_mock.return_value = server_mock
        server_mock.accept.side_effect = [(None, None)]
        N_workers = 8

        server = Server(N_workers)
        server.start()
        self.assertEqual(N_workers, thread_mock.call_count)
