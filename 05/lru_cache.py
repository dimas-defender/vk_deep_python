class LRUCache:
    def __init__(self, limit=42):
        self.cache = {}
        self.limit = limit
        self.order = []

    def get(self, key):
        try:
            value = self.cache[key]
            self.__update_order(key)
            return value
        except KeyError:
            return None

    def set(self, key, value):
        self.cache[key] = value
        self.__update_order(key)

    def __update_order(self, key):
        try:
            self.order.remove(key)
        except ValueError:
            pass

        self.order.append(key)
        if len(self.order) > self.limit:
            old_key = self.order.pop(0)
            self.cache.pop(old_key)
