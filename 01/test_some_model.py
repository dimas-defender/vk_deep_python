from unittest import mock, TestCase
from some_model import SomeModel, predict_message_mood


class TestSomeModel(TestCase):
    def setUp(self):
        self.model = SomeModel()

    def test_predict_invalid(self):
        result = predict_message_mood("test", self.model, -0.2, 0.4)
        self.assertEqual(result, "Некорректные аргументы")

    def test_predict_wrong_thresholds(self):
        result = predict_message_mood("string", self.model, 0.6, 0.4)
        self.assertEqual(result, "Некорректные аргументы")

    def test_predict_great(self):
        with mock.patch("someModel.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.7

            result = predict_message_mood("abcdefg", self.model, 0.2, 0.6)
            self.assertEqual(result, "отл")
            expected_calls = [
                mock.call("abcdefg")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_predict_poor(self):
        with mock.patch("someModel.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.2

            result = predict_message_mood("Kk", self.model, 0.3, 0.8)
            self.assertEqual(result, "неуд")
            expected_calls = [
                mock.call("Kk")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_predict_normal(self):
        with mock.patch("someModel.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5

            result = predict_message_mood("qWeRt", self.model, 0.4, 0.8)
            self.assertEqual(result, "норм")
            expected_calls = [
                mock.call("qWeRt")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_predict_normal_edge(self):
        with mock.patch("someModel.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.6

            result = predict_message_mood("qWeRtY", self.model, 0.3, 0.6)
            self.assertEqual(result, "норм")
            expected_calls = [
                mock.call("qWeRtY")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)
