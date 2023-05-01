from unittest import mock, IsolatedAsyncioTestCase
from fetcher import fetch_batch


class AsyncTest(IsolatedAsyncioTestCase):
    async def test_fetch_batch(self):
        urls = [
            'https://pythonworld.ru\n',
            'https://www.google.ru\n',
            'https://www.canon.ru/\n',
            'https://www.mathworks.com/\n',
            'https://www.rambler.ru/\n'
        ]
        workers = 3

        resp_mock = mock.AsyncMock()
        resp_mock.read.return_value = "some html data"
        resp_mock.status = 200

        get_mock = mock.MagicMock()
        get_mock.__aenter__.return_value = resp_mock

        session_mock = mock.Mock()
        session_mock.get.return_value = get_mock

        await fetch_batch(urls, workers, session_mock)

        self.assertEqual(resp_mock.read.call_count, 5)
        self.assertEqual(session_mock.get.call_count, 5)
