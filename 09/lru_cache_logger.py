import logging
import argparse


class LRUCache:
    def __init__(self, limit=42):
        self.cache = {}
        self.limit = limit
        logger.debug("Init LRU Cache")

    def get(self, key):
        try:
            value = self.cache.pop(key)
            logger.debug("Key=%s removed from cache", key)
            self.cache[key] = value
            logger.debug("Key=%s added to cache with value=%s", key, value)
            logger.info("GET key=%s from cache", key)
            return value
        except KeyError:
            logger.error("NO KEY=%s in cache", key)
            return None

    def set(self, key, value):
        old_value = self.cache.pop(key, None)
        self.cache[key] = value

        if old_value:
            logger.info("SET value=%s for old key=%s", value, key)
            logger.debug("Key=%s removed from cache", key)
        else:
            logger.info("SET new key=%s with value=%s", key, value)

        logger.debug("Key=%s added to cache with value=%s", key, value)

        if len(self.cache) > self.limit:
            logger.info("Cache size limit reached with new key=%s", key)
            first_key = next(iter(self.cache))
            self.cache.pop(first_key)
            logger.info("LRU key=%s removed from cache", first_key)


class MessageLengthFilter(logging.Filter):
    def filter(self, record):
        return len(record.msg) < 30


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", action="store_true")
    parser.add_argument("-f", action="store_true")
    args = parser.parse_args()

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    FILE_FMT_STRING = "%(asctime)s\t%(levelname)s\t[file]\t%(message)s"
    format_file = logging.Formatter(FILE_FMT_STRING)
    file_handler = logging.FileHandler("cache.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(format_file)
    logger.addHandler(file_handler)

    if args.s:
        STD_FMT_STRING = "%(asctime)s\t%(levelname)s\t[stdout]\t%(message)s"
        format_stdout = logging.Formatter(STD_FMT_STRING)
        std_handler = logging.StreamHandler()
        std_handler.setLevel(logging.INFO)
        std_handler.setFormatter(format_stdout)
        logger.addHandler(std_handler)

    if args.f:
        logger.addFilter(MessageLengthFilter())

    cache = LRUCache(2)
    cache.set("k1", "val1")
    cache.get("k1")
    cache.get("k2")
    cache.set("k2", "val2")
    cache.set("k1", "new_val")
    cache.set("k3", "val3")
