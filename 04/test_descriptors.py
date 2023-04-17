from unittest import TestCase
from descriptors import Car


class TestDescriptors(TestCase):
    def setUp(self):
        self.car = Car("Skoda Octavia", 2016, 1.8)

    def test_model_get_ok(self):
        value = self.car.model
        self.assertEqual(value, "Skoda Octavia")

    def test_model_get_none(self):
        with self.assertRaises(TypeError):
            Car.model

    def test_model_set_ok(self):
        self.car.model = "BMW"
        self.assertEqual(self.car.model, "BMW")

    def test_model_set_wrong_type(self):
        with self.assertRaises(TypeError):
            self.car.model = 123
        self.assertEqual(self.car.model, "Skoda Octavia")

    def test_model_set_too_short(self):
        with self.assertRaises(ValueError):
            self.car.model = "AB"
        self.assertEqual(self.car.model, "Skoda Octavia")

    def test_model_set_not_upper(self):
        with self.assertRaises(ValueError):
            self.car.model = "renault Logan"
        self.assertEqual(self.car.model, "Skoda Octavia")

    def test_model_del_ok(self):
        del self.car.model
        with self.assertRaises(AttributeError):
            self.car.model

    def test_year_get_ok(self):
        value = self.car.manufactured
        self.assertEqual(value, 2016)

    def test_year_get_none(self):
        with self.assertRaises(TypeError):
            Car.manufactured

    def test_year_set_ok_top_edge(self):
        self.car.manufactured = 2023
        self.assertEqual(self.car.manufactured, 2023)

    def test_year_set_ok_bottom_edge(self):
        self.car.manufactured = 1900
        self.assertEqual(self.car.manufactured, 1900)

    def test_year_set_wrong_type(self):
        with self.assertRaises(TypeError):
            self.car.manufactured = 5.5
        self.assertEqual(self.car.manufactured, 2016)

    def test_year_set_low_value(self):
        with self.assertRaises(ValueError):
            self.car.manufactured = 1850
        self.assertEqual(self.car.manufactured, 2016)

    def test_year_set_high_value(self):
        with self.assertRaises(ValueError):
            self.car.manufactured = 2025
        self.assertEqual(self.car.manufactured, 2016)

    def test_year_del_ok(self):
        del self.car.manufactured
        with self.assertRaises(AttributeError):
            self.car.manufactured

    def test_size_get_ok(self):
        value = self.car.engine_size
        self.assertEqual(value, 1.8)

    def test_size_get_none(self):
        with self.assertRaises(TypeError):
            Car.engine_size

    def test_size_set_ok_top_edge(self):
        self.car.engine_size = 6.0
        self.assertEqual(self.car.engine_size, 6.0)

    def test_size_set_ok_bottom_edge(self):
        self.car.engine_size = 0.5
        self.assertEqual(self.car.engine_size, 0.5)

    def test_size_set_wrong_type(self):
        with self.assertRaises(TypeError):
            self.car.engine_size = True
        self.assertEqual(self.car.engine_size, 1.8)

    def test_size_set_low_value(self):
        with self.assertRaises(ValueError):
            self.car.engine_size = 0.3
        self.assertEqual(self.car.engine_size, 1.8)

    def test_size_set_high_value(self):
        with self.assertRaises(ValueError):
            self.car.engine_size = 6.4
        self.assertEqual(self.car.engine_size, 1.8)

    def test_size_del_ok(self):
        del self.car.engine_size
        with self.assertRaises(AttributeError):
            self.car.engine_size
