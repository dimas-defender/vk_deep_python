from unittest import TestCase
from file_filter import filter_file


class TestFileFilter(TestCase):
    def test_success(self):
        words = ["cAR", "empTy", "ReD", "goblin"]
        expected = ['word Test car long dOoR\n', 'crew reD pHOne wave waTer\n']
        with open("data.txt", "r") as file:
            result = list(filter_file(file, words))
            self.assertEqual(result, expected)

    def test_success_filename(self):
        words = ["cAR", "empTy", "ReD", "goblin"]
        expected = ['word Test car long dOoR\n', 'crew reD pHOne wave waTer\n']
        result = list(filter_file("data.txt", words))
        self.assertEqual(result, expected)

    def test_success_few_words_in_one_row(self):
        words = ["cAR", "loNG", "ReD", "goblin"]
        expected = ['word Test car long dOoR\n', 'crew reD pHOne wave waTer\n']
        with open("data.txt", "r") as file:
            result = list(filter_file(file, words))
            self.assertEqual(result, expected)

    def test_success_one_row(self):
        words = ["active", "raNGE", "tempo", "CLimb"]
        expected = ['grEEn VAlue throw Range\n']
        with open("data.txt", "r") as file:
            result = list(filter_file(file, words))
            self.assertEqual(result, expected)

    def test_no_words(self):
        words = []
        expected = []
        with open("data.txt", "r") as file:
            result = list(filter_file(file, words))
            self.assertEqual(result, expected)

    def test_empty_result(self):
        words = ["active", "ramBO", "tempo", "CLimb"]
        expected = []
        with open("data.txt", "r") as file:
            result = list(filter_file(file, words))
            self.assertEqual(result, expected)
