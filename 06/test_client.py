from unittest import TestCase, mock
from client import Client


class TestClient(TestCase):
    @mock.patch('socket.socket')
    def test_send_request(self, socket_mock):
        urls = [
            'https://vk.com\n',
            'https://mail.ru\n'
        ]

        client = Client(urls)

        socket_mock.return_value = socket_mock
        socket_mock.recv.side_effect = [
            "{\"Вконтакте\": 5}".encode(),
            "{\"в\": 46}".encode()
        ]

        client.fill_queue()
        self.assertEqual(socket_mock.call_count, 2)
        socket_mock.recv.assert_called_with(4096)
        self.assertEqual(socket_mock.close.call_count, 2)
        self.assertEqual(client.url_queue.qsize(), 1)
        self.assertEqual(client.url_queue.get(), 'EOF')

    @mock.patch('threading.Thread')
    def test_thread(self, thread_mock):
        thread_mock.return_value = thread_mock

        N_threads = 3
        client = Client(['EOF'], N_threads)

        self.assertEqual(N_threads, thread_mock.call_count)
        self.assertEqual(N_threads, thread_mock.start.call_count)

        self.assertEqual(0, thread_mock.join.call_count)
        client.fill_queue()
        self.assertEqual(N_threads, thread_mock.join.call_count)
