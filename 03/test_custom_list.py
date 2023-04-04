from unittest import TestCase
from custom_list import CustomList


class TestCustomList(TestCase):
    def test_add_both_custom(self):
        list1 = CustomList([5, 1, 3, 7])
        list2 = CustomList([1, 2, 7])
        expected = CustomList([6, 3, 10, 7])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))

    def test_add_built_in_and_custom(self):
        list1 = CustomList([1])
        list2 = [2, 5]
        expected = CustomList([3, 5])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))

    def test_radd(self):
        list1 = [2, 5]
        list2 = CustomList([1])
        expected = CustomList([3, 5])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))

    def test_sub_both_custom(self):
        list1 = CustomList([5, 1, 3, 7])
        list2 = CustomList([1, 2, 7])
        expected = CustomList([4, -1, -4, 7])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))

    def test_sub_built_in_and_custom(self):
        list1 = CustomList([1])
        list2 = [2, 5]
        expected = CustomList([-1, -5])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))

    def test_rsub(self):
        list1 = [2, 5]
        list2 = CustomList([1])
        expected = CustomList([1, 5])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))

    def test_equal(self):
        list1 = CustomList([5, 12, -3, 8])
        list2 = CustomList([16, -4, 10])
        self.assertEqual(list1 == list2, True)

    def test_not_equal(self):
        list1 = CustomList([5, 12, -3, 8])
        list2 = CustomList([0, 22, 0, 0, 0])
        self.assertEqual(list1 != list2, False)

    def test_greater(self):
        list1 = CustomList([5, 14, -3, 8])
        list2 = CustomList([16, -4, 10, 0, 1])
        self.assertEqual(list1 > list2, True)

    def test_greater_or_equal(self):
        list1 = CustomList([22])
        list2 = CustomList([16, -4, 10])
        self.assertEqual(list1 >= list2, True)

    def test_less(self):
        list1 = CustomList([5, 12, -3, 15])
        list2 = CustomList([16, -4, 10])
        self.assertEqual(list1 < list2, False)

    def test_less_or_equal(self):
        list1 = CustomList([5, 12, -3, 5])
        list2 = CustomList([16, -4, 10])
        self.assertEqual(list1 <= list2, True)

    def test_str(self):
        list1 = CustomList([5, 12, -7, 25])
        expected = "Items: [5, 12, -7, 25] Sum: 35"
        self.assertEqual(str(list1), expected)
