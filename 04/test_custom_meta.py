from unittest import TestCase
from custom_meta import CustomMeta


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

    def __str__(self):
        return "Custom_by_metaclass"


class TestCustomMeta(TestCase):
    def setUp(self):
        self.inst = CustomClass()

    def test_cls_attr_old(self):
        with self.assertRaises(AttributeError):
            CustomClass.x

    def test_cls_attr_new(self):
        self.assertEqual(CustomClass.custom_x, 50)

    def test_cls_dynamic(self):
        CustomClass.dynamic = "after init"
        with self.assertRaises(AttributeError):
            CustomClass.dynamic
        self.assertEqual(CustomClass.custom_dynamic, "after init")

    def test_cls_attr_old_from_inst(self):
        with self.assertRaises(AttributeError):
            self.inst.x

    def test_cls_attr_new_from_inst(self):
        self.assertEqual(self.inst.custom_x, 50)

    def test_inst_attr_old(self):
        with self.assertRaises(AttributeError):
            self.inst.val

    def test_inst_attr_new(self):
        self.assertEqual(self.inst.custom_val, 99)

    def test_inst_method_old(self):
        with self.assertRaises(AttributeError):
            self.inst.line()

    def test_inst_method_new(self):
        self.assertEqual(self.inst.custom_line(), 100)

    def test_inst_magic_method(self):
        self.assertEqual(str(self.inst), "Custom_by_metaclass")

    def test_inst_nonexistent_attr(self):
        with self.assertRaises(AttributeError):
            self.inst.aaa

    def test_inst_dynamic(self):
        self.inst.dynamic = "added later"
        with self.assertRaises(AttributeError):
            self.inst.dynamic
        self.assertEqual(self.inst.custom_dynamic, "added later")
