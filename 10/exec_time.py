import json
from time import time

import ujson

import cjson


def benchmark_loads():
    data = open("data.json", "r")

    start = time()
    for item in data:
        json.loads(item.strip())
    end = time()
    time_json = end - start

    data.seek(0)
    start = time()
    for item in data:
        ujson.loads(item.strip())
    end = time()
    time_ujson = end - start

    data.seek(0)
    start = time()
    for item in data:
        cjson.loads(item.strip())
    end = time()
    time_cjson = end - start

    data.close()

    print("Json.loads time:", time_json)
    print("Ujson.loads time:", time_ujson)
    print("Cjson.loads time:", time_cjson)


if __name__ == "__main__":
    benchmark_loads()
