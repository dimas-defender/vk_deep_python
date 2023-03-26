from unittest import mock, TestCase
from parse_json import parse_json


class TestJsonParser(TestCase):
    def test_success(self):
        mock_callback = mock.Mock()
        json_str = '{"key1": "driving a car", "key2": "apple orange"}'
        fields = ['key1', 'extra', 'key2']
        words = ['orange', 'car']

        result = parse_json(json_str, mock_callback, fields, words)
        self.assertEqual(result, None)
        self.assertEqual(mock_callback.call_count, 2)

        expected_calls = [
            mock.call('key1', 'car'),
            mock.call('key2', 'orange')
        ]
        self.assertEqual(expected_calls, mock_callback.mock_calls)

    def test_invalid_json(self):
        mock_callback = mock.Mock()
        json_str = "broken json string"
        fields = ['key1', 'key2']
        words = ['orange', 'car']

        result = parse_json(json_str, mock_callback, fields, words)
        self.assertEqual(result, "Передана некорректная json-строка!")
        self.assertEqual(mock_callback.call_count, 0)

    def test_fields_none(self):
        mock_callback = mock.Mock()
        json_str = '{"key1": "driving a car", "key2": "apple orange"}'
        words = ['orange', 'car']

        result = parse_json(json_str, mock_callback, None, words)
        self.assertEqual(result, "Ничего не может быть найдено!")
        self.assertEqual(mock_callback.call_count, 0)

    def test_words_none(self):
        mock_callback = mock.Mock()
        json_str = '{"key1": "driving a car", "key2": "apple orange"}'
        fields = ['key1', 'key2']

        result = parse_json(json_str, mock_callback, fields)
        self.assertEqual(result, "Ничего не может быть найдено!")
        self.assertEqual(mock_callback.call_count, 0)

    def test_wrong_fields(self):
        mock_callback = mock.Mock()
        json_str = '{"key1": "driving a car", "key2": "apple orange"}'
        fields = ['keyw31', 'apple']
        words = ['orange', 'car']

        result = parse_json(json_str, mock_callback, fields, words)
        self.assertEqual(result, None)
        self.assertEqual(mock_callback.call_count, 0)

    def test_nothing_found(self):
        mock_callback = mock.Mock()
        json_str = '{"key1": "driving a car", "key2": "apple orange"}'
        fields = ['key1', 'extra', 'key2']
        words = ['pine', 'cycle']

        result = parse_json(json_str, mock_callback, fields, words)
        self.assertEqual(result, None)
        self.assertEqual(mock_callback.call_count, 0)
