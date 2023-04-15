from unittest import TestCase
from custom_list import CustomList


class TestCustomList(TestCase):
    def test_add_both_custom_same_len(self):
        list1 = CustomList([5, 1, 3])
        list2 = CustomList([1, 2, 7])
        expected = CustomList([6, 3, 10])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [5, 1, 3])
        self.assertEqual(list(list2), [1, 2, 7])

    def test_add_both_custom_shorter(self):
        list1 = CustomList([5, 1, 3, 7])
        list2 = CustomList([1, 2, 7])
        expected = CustomList([6, 3, 10, 7])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [5, 1, 3, 7])
        self.assertEqual(list(list2), [1, 2, 7])

    def test_add_both_custom_longer(self):
        list1 = CustomList([5, 1, 3, 7])
        list2 = CustomList([1, 2, 7, 0, -10])
        expected = CustomList([6, 3, 10, 7, -10])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [5, 1, 3, 7])
        self.assertEqual(list(list2), [1, 2, 7, 0, -10])

    def test_add_built_in_and_custom_same_len(self):
        list1 = CustomList([1, -3])
        list2 = [2, 5]
        expected = CustomList([3, 2])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [1, -3])
        self.assertEqual(list2, [2, 5])

    def test_add_built_in_and_custom_shorter(self):
        list1 = CustomList([1, 15, -23])
        list2 = [2, 5]
        expected = CustomList([3, 20, -23])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [1, 15, -23])
        self.assertEqual(list2, [2, 5])

    def test_add_built_in_and_custom_longer(self):
        list1 = CustomList([1])
        list2 = [2, 5]
        expected = CustomList([3, 5])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [1])
        self.assertEqual(list2, [2, 5])

    def test_radd_same_len(self):
        list1 = [2, 5]
        list2 = CustomList([1, -24])
        expected = CustomList([3, -19])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list1, [2, 5])
        self.assertEqual(list(list2), [1, -24])

    def test_radd_shorter(self):
        list1 = [2, 5]
        list2 = CustomList([1])
        expected = CustomList([3, 5])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list1, [2, 5])
        self.assertEqual(list(list2), [1])

    def test_radd_longer(self):
        list1 = [2, 5]
        list2 = CustomList([1, -31, 1])
        expected = CustomList([3, -26, 1])

        result = list1 + list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list1, [2, 5])
        self.assertEqual(list(list2), [1, -31, 1])

    def test_sub_both_custom_same_len(self):
        list1 = CustomList([5, 1, 3])
        list2 = CustomList([1, 2, 7])
        expected = CustomList([4, -1, -4])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [5, 1, 3])
        self.assertEqual(list(list2), [1, 2, 7])

    def test_sub_both_custom_shorter(self):
        list1 = CustomList([5, 1, 3, 7])
        list2 = CustomList([1, 2, 7])
        expected = CustomList([4, -1, -4, 7])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [5, 1, 3, 7])
        self.assertEqual(list(list2), [1, 2, 7])

    def test_sub_both_custom_longer(self):
        list1 = CustomList([5, 1, 3, 7])
        list2 = CustomList([1, 2, 7, -11, 0])
        expected = CustomList([4, -1, -4, 18, 0])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [5, 1, 3, 7])
        self.assertEqual(list(list2), [1, 2, 7, -11, 0])

    def test_sub_built_in_and_custom_same_len(self):
        list1 = CustomList([1, -7])
        list2 = [2, 5]
        expected = CustomList([-1, -12])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [1, -7])
        self.assertEqual(list2, [2, 5])

    def test_sub_built_in_and_custom_shorter(self):
        list1 = CustomList([1, 14, 21])
        list2 = [2, 5]
        expected = CustomList([-1, 9, 21])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [1, 14, 21])
        self.assertEqual(list2, [2, 5])

    def test_sub_built_in_and_custom_longer(self):
        list1 = CustomList([1])
        list2 = [2, 5]
        expected = CustomList([-1, -5])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list(list1), [1])
        self.assertEqual(list2, [2, 5])

    def test_rsub_same_len(self):
        list1 = [2, 5]
        list2 = CustomList([1, 20])
        expected = CustomList([1, -15])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list1, [2, 5])
        self.assertEqual(list(list2), [1, 20])

    def test_rsub_shorter(self):
        list1 = [2, 5]
        list2 = CustomList([1])
        expected = CustomList([1, 5])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list1, [2, 5])
        self.assertEqual(list(list2), [1])

    def test_rsub_longer(self):
        list1 = [2, 5]
        list2 = CustomList([1, -1, 29])
        expected = CustomList([1, 6, -29])

        result = list1 - list2
        self.assertEqual(list(result), list(expected))
        self.assertEqual(list1, [2, 5])
        self.assertEqual(list(list2), [1, -1, 29])

    def test_equal(self):
        list1 = CustomList([5, 12, -3, 8])
        list2 = CustomList([16, -4, 10])

        self.assertEqual(list1 == list2, True)
        self.assertEqual(list(list1), [5, 12, -3, 8])
        self.assertEqual(list(list2), [16, -4, 10])

    def test_not_equal(self):
        list1 = CustomList([5, 12, -3, 8])
        list2 = CustomList([0, 22, 0, 0, 0])

        self.assertEqual(list1 != list2, False)
        self.assertEqual(list(list1), [5, 12, -3, 8])
        self.assertEqual(list(list2), [0, 22, 0, 0, 0])

    def test_greater(self):
        list1 = CustomList([5, 14, -3, 8])
        list2 = CustomList([16, -4, 10, 0, 1])

        self.assertEqual(list1 > list2, True)
        self.assertEqual(list(list1), [5, 14, -3, 8])
        self.assertEqual(list(list2), [16, -4, 10, 0, 1])

    def test_greater_or_equal(self):
        list1 = CustomList([22])
        list2 = CustomList([16, -4, 10])

        self.assertEqual(list1 >= list2, True)
        self.assertEqual(list(list1), [22])
        self.assertEqual(list(list2), [16, -4, 10])

    def test_less(self):
        list1 = CustomList([5, 12, -3, 15])
        list2 = CustomList([16, -4, 10])

        self.assertEqual(list1 < list2, False)
        self.assertEqual(list(list1), [5, 12, -3, 15])
        self.assertEqual(list(list2), [16, -4, 10])

    def test_less_or_equal(self):
        list1 = CustomList([5, 12, -3, 5])
        list2 = CustomList([16, -4, 10])

        self.assertEqual(list1 <= list2, True)
        self.assertEqual(list(list1), [5, 12, -3, 5])
        self.assertEqual(list(list2), [16, -4, 10])

    def test_str(self):
        list1 = CustomList([5, 12, -7, 25])
        expected = "Items: [5, 12, -7, 25] Sum: 35"

        self.assertEqual(str(list1), expected)
        self.assertEqual(list(list1), [5, 12, -7, 25])
