from unittest import TestCase
from lru_cache import LRUCache


class TestLRUCache(TestCase):
    def test_success(self):
        cache = LRUCache(2)
        cache.set("k1", "val1")
        cache.set("k2", "val2")

        self.assertIsNone(cache.get("k3"))
        self.assertEqual(cache.get("k2"), "val2")
        self.assertEqual(cache.get("k1"), "val1")

        cache.set("k3", "val3")

        self.assertEqual(cache.get("k3"), "val3")
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k1"), "val1")

    def test_len_1(self):
        cache = LRUCache(1)
        cache.set("k1", "val1")

        self.assertEqual(cache.get("k1"), "val1")
        self.assertIsNone(cache.get("k2"))
        self.assertIsNone(cache.get("k3"))

        cache.set("k2", "val2")
        cache.set("k3", "val3")

        self.assertIsNone(cache.get("k1"))
        self.assertIsNone(cache.get("k2"))
        self.assertEqual(cache.get("k3"), "val3")

    def test_reset_key(self):
        cache = LRUCache(2)
        cache.set("login", "maestro")
        cache.set("password", "hidden")

        cache.set("login", "skipper")
        cache.set("email", "unknown")

        self.assertEqual(cache.get("login"), "skipper")
        self.assertEqual(cache.get("email"), "unknown")
        self.assertIsNone(cache.get("password"))
