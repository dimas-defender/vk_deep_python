from unittest import mock, TestCase
from some_model import SomeModel, predict_message_mood


class TestSomeModel(TestCase):
    def setUp(self):
        self.model = SomeModel()

    def test_predict_invalid_bad_threshold(self):
        result = predict_message_mood("test", self.model, -0.2, 0.4)
        self.assertEqual(result, "Некорректные аргументы")

    def test_predict_invalid_good_threshold(self):
        result = predict_message_mood("test", self.model, 0.2, 1.2)
        self.assertEqual(result, "Некорректные аргументы")

    def test_predict_wrong_thresholds(self):
        result = predict_message_mood("string", self.model, 0.6, 0.4)
        self.assertEqual(result, "Некорректные аргументы")

    def test_predict_great(self):
        with mock.patch("some_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.7

            result = predict_message_mood("abcdefg", self.model, 0.2, 0.6)
            self.assertEqual(result, "отл")
            expected_calls = [
                mock.call("abcdefg")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_predict_poor(self):
        with mock.patch("some_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.2

            result = predict_message_mood("Kk", self.model, 0.3, 0.8)
            self.assertEqual(result, "неуд")
            expected_calls = [
                mock.call("Kk")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_predict_normal(self):
        with mock.patch("some_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5

            result = predict_message_mood("qWeRt", self.model, 0.4, 0.8)
            self.assertEqual(result, "норм")
            expected_calls = [
                mock.call("qWeRt")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_predict_top_edge(self):
        with mock.patch("some_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.6

            result = predict_message_mood("qWeRtY", self.model, 0.3, 0.6)
            self.assertEqual(result, "норм")
            expected_calls = [
                mock.call("qWeRtY")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_predict_bottom_edge(self):
        with mock.patch("some_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.4

            result = predict_message_mood("TwIN", self.model, 0.4, 0.7)
            self.assertEqual(result, "норм")
            expected_calls = [
                mock.call("TwIN")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)

    def test_predict_edge_thresholds(self):
        with mock.patch("some_model.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.5

            result = predict_message_mood("TwINs", self.model, 0, 1)
            self.assertEqual(result, "норм")
            expected_calls = [
                mock.call("TwINs")
            ]
            self.assertEqual(expected_calls, mock_predict.mock_calls)
