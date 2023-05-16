from unittest import TestCase, mock
from io import StringIO
from client import Client


class TestClient(TestCase):
    @mock.patch('socket.socket')
    def test_send_request(self, socket_mock):
        responses = StringIO()
        urls = [
            "https://vk.com\n",
            "https://mail.ru\n"
        ]

        n_threads = 2
        client = Client(urls, n_threads, responses)

        socket_mock.return_value = socket_mock
        socket_mock.recv.side_effect = [
            "{'Вконтакте': 5}".encode(),
            "{'в': 46}".encode()
        ]

        client.fill_queue()

        send_expected_calls = [
            mock.call("https://vk.com".encode()),
            mock.call("https://mail.ru".encode())
        ]
        self.assertEqual(send_expected_calls, socket_mock.sendall.mock_calls)

        resp_exp_value = "https://vk.com: {'Вконтакте': 5}\nhttps://mail.ru: {'в': 46}\n"
        self.assertEqual(responses.getvalue(), resp_exp_value)

        self.assertEqual(socket_mock.call_count, 2)
        socket_mock.recv.assert_called_with(4096)
        self.assertEqual(socket_mock.close.call_count, 2)
        self.assertEqual(client.url_queue.qsize(), 1)
        self.assertEqual(client.url_queue.get(), "EOF")

    @mock.patch('threading.Thread')
    def test_create_some_threads(self, thread_mock):
        thread_mock.return_value = thread_mock

        n_threads = 6
        client = Client([], n_threads)

        self.assertEqual(n_threads, thread_mock.call_count)
        self.assertEqual(n_threads, thread_mock.start.call_count)
        self.assertEqual(0, thread_mock.join.call_count)
        client.fill_queue()
        self.assertEqual(n_threads, thread_mock.join.call_count)
        self.assertEqual(client.url_queue.qsize(), 1)
        self.assertEqual(client.url_queue.get(), "EOF")

    @mock.patch('threading.Thread')
    def test_create_one_thread(self, thread_mock):
        thread_mock.return_value = thread_mock

        n_threads = 1
        client = Client([], n_threads)

        self.assertEqual(n_threads, thread_mock.call_count)
        self.assertEqual(n_threads, thread_mock.start.call_count)
        self.assertEqual(0, thread_mock.join.call_count)
        client.fill_queue()
        self.assertEqual(n_threads, thread_mock.join.call_count)
        self.assertEqual(client.url_queue.qsize(), 1)
        self.assertEqual(client.url_queue.get(), "EOF")
