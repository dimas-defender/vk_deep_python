class LRUCache:
    def __init__(self, limit=42):
        self.cache = {}
        self.limit = limit

    def get(self, key):
        try:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        except KeyError:
            return None

    def set(self, key, value):
        self.cache.pop(key, None)
        self.cache[key] = value

        if len(self.cache) > self.limit:
            first_key = next(iter(self.cache))
            self.cache.pop(first_key)
