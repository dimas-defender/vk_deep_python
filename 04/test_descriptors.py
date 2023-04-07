from unittest import TestCase
from descriptors import Car


class TestDescriptors(TestCase):
    def setUp(self):
        self.car = Car("Skoda Octavia", 2016, 1.8)

    def test_model_get_ok(self):
        value = self.car.model
        self.assertEqual(value, "Skoda Octavia")

    def test_model_get_none(self):
        try:
            Car.model
            self.fail()
        except TypeError:
            pass

    def test_model_set_ok(self):
        self.car.model = "BMW"
        self.assertEqual(self.car.model, "BMW")

    def test_model_set_wrong_type(self):
        try:
            self.car.model = 123
            self.fail()
        except TypeError:
            pass

    def test_model_set_too_short(self):
        try:
            self.car.model = "AB"
            self.fail()
        except ValueError:
            pass

    def test_model_set_not_upper(self):
        try:
            self.car.model = "renault Logan"
            self.fail()
        except ValueError:
            pass

    def test_model_del_ok(self):
        del self.car.model
        try:
            self.car.model
            self.fail()
        except AttributeError:
            pass

    def test_year_get_ok(self):
        value = self.car.manufactured
        self.assertEqual(value, 2016)

    def test_year_get_none(self):
        try:
            Car.manufactured
            self.fail()
        except TypeError:
            pass

    def test_year_set_ok_top_edge(self):
        self.car.manufactured = 2023
        self.assertEqual(self.car.manufactured, 2023)

    def test_year_set_ok_bottom_edge(self):
        self.car.manufactured = 1900
        self.assertEqual(self.car.manufactured, 1900)

    def test_year_set_wrong_type(self):
        try:
            self.car.manufactured = 5.5
            self.fail()
        except TypeError:
            pass

    def test_year_set_low_value(self):
        try:
            self.car.manufactured = 1850
            self.fail()
        except ValueError:
            pass

    def test_year_set_high_value(self):
        try:
            self.car.manufactured = 2025
            self.fail()
        except ValueError:
            pass

    def test_year_del_ok(self):
        del self.car.manufactured
        try:
            self.car.manufactured
            self.fail()
        except AttributeError:
            pass

    def test_size_get_ok(self):
        value = self.car.engine_size
        self.assertEqual(value, 1.8)

    def test_size_get_none(self):
        try:
            Car.engine_size
            self.fail()
        except TypeError:
            pass

    def test_size_set_ok_top_edge(self):
        self.car.engine_size = 6.0
        self.assertEqual(self.car.engine_size, 6.0)

    def test_size_set_ok_bottom_edge(self):
        self.car.engine_size = 0.5
        self.assertEqual(self.car.engine_size, 0.5)

    def test_size_set_wrong_type(self):
        try:
            self.car.engine_size = True
            self.fail()
        except TypeError:
            pass

    def test_size_set_low_value(self):
        try:
            self.car.engine_size = 0.3
            self.fail()
        except ValueError:
            pass

    def test_size_set_high_value(self):
        try:
            self.car.engine_size = 6.4
            self.fail()
        except ValueError:
            pass

    def test_size_del_ok(self):
        del self.car.engine_size
        try:
            self.car.engine_size
            self.fail()
        except AttributeError:
            pass
