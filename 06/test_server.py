from unittest import TestCase, mock
from server import Server


class TestServer(TestCase):
    @mock.patch('socket.socket')
    def test_handle_request(self, server_mock):
        client_mock = mock.Mock()
        client_mock.recv.side_effect = [
            "https://vk.com".encode(),
            "https://google.ru".encode(),
            "https://yandex.com".encode()
        ]

        server_mock.return_value = server_mock
        server_mock.accept.side_effect = [
            (client_mock, None),
            (client_mock, None),
            (client_mock, None),
            (None, None)
        ]

        url_handler_mock = mock.Mock()
        url_handler_mock.side_effect = [
            "{'ВКонтакте': 3, 'браузер': 2}",
            "{'GoogleПоиск': 1, 'Картинки': 1}",
            "{'com': 2, 'YandexenBahasa': 1}"
        ]

        n_workers = 3
        n_words = 2
        server = Server(n_workers, n_words, url_handler_mock)
        server.start()

        handler_expected_calls = [
            mock.call("https://vk.com", n_words),
            mock.call("https://google.ru", n_words),
            mock.call("https://yandex.com", n_words)
        ]
        self.assertEqual(handler_expected_calls, url_handler_mock.mock_calls)

        send_expected_calls = [
            mock.call("{'ВКонтакте': 3, 'браузер': 2}".encode()),
            mock.call("{'GoogleПоиск': 1, 'Картинки': 1}".encode()),
            mock.call("{'com': 2, 'YandexenBahasa': 1}".encode())
        ]
        self.assertEqual(send_expected_calls, client_mock.sendall.mock_calls)

        self.assertEqual(4, server_mock.accept.call_count)
        self.assertEqual(3, client_mock.recv.call_count)
        self.assertEqual(3, url_handler_mock.call_count)
        self.assertEqual(3, server.urls_handled)

    @mock.patch("socket.socket")
    @mock.patch("threading.Thread")
    def test_create_some_threads(self, thread_mock, server_mock):
        thread_mock.return_value = thread_mock
        server_mock.return_value = server_mock
        server_mock.accept.side_effect = [(None, None)]
        n_workers = 8

        server = Server(n_workers)
        server.start()
        self.assertEqual(n_workers, thread_mock.call_count)
        self.assertEqual(n_workers, thread_mock.start.call_count)
        self.assertEqual(n_workers, thread_mock.join.call_count)

    @mock.patch("socket.socket")
    @mock.patch("threading.Thread")
    def test_create_one_thread(self, thread_mock, server_mock):
        thread_mock.return_value = thread_mock
        server_mock.return_value = server_mock
        server_mock.accept.side_effect = [(None, None)]
        n_workers = 1

        server = Server(n_workers)
        server.start()
        self.assertEqual(n_workers, thread_mock.call_count)
        self.assertEqual(n_workers, thread_mock.start.call_count)
        self.assertEqual(n_workers, thread_mock.join.call_count)
