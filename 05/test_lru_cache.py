from unittest import TestCase
from lru_cache import LRUCache


class TestLRUCache(TestCase):
    def setUp(self):
        self.cache = LRUCache(2)
        self.cache.set("login", "maestro")

    def test_get_none(self):
        self.assertIsNone(self.cache.get("not_in_cache"))

    def test_get_ok(self):
        self.assertEqual(self.cache.get("login"), "maestro")

    def test_set_new_key(self):
        self.cache.set("password", "hidden")
        self.assertEqual(self.cache.get("password"), "hidden")
        self.assertEqual(self.cache.get("login"), "maestro")

    def test_set_old_key(self):
        self.cache.set("login", "skipper")
        self.assertEqual(self.cache.get("login"), "skipper")

    def test_set_over_limit(self):
        self.cache.set("password", "hidden")
        self.assertEqual(self.cache.get("password"), "hidden")
        self.assertEqual(self.cache.get("login"), "maestro")
        self.assertIsNone(self.cache.get("email"))

        self.cache.set("email", "unknown")
        self.assertIsNone(self.cache.get("password"))
        self.assertEqual(self.cache.get("login"), "maestro")
        self.assertEqual(self.cache.get("email"), "unknown")
