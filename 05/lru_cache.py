class LRUCache:
    def __init__(self, limit=42):
        self.cache = {}
        self.limit = limit
        self.order = {}
        self.timestamp = 0

    def get(self, key):
        try:
            value = self.cache[key]
            self.order[key] = self.timestamp
            self.timestamp += 1
            return value
        except KeyError:
            return None

    def set(self, key, value):
        self.cache[key] = value
        self.order[key] = self.timestamp
        self.timestamp += 1

        if len(self.order) > self.limit:
            old_key = min(self.order.keys(), key=lambda x: self.order[x])
            self.order.pop(old_key)
            self.cache.pop(old_key)
