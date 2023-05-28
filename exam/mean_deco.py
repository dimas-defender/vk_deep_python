from collections import deque
from time import time, sleep
from random import random


def mean_deco(k):
    def mean_time(func):
        recent_calls = deque(maxlen=k)
        def inner(*args, **kwargs):
            start = time()
            result = func(*args, **kwargs)
            end = time()

            exec_time = end - start
            recent_calls.append(exec_time)
            #print(f"Execution time: {exec_time:.3f}s")

            if len(recent_calls) >= k:
                print(f"Mean execution time for latest {k} calls: {sum(recent_calls) / k :.3f}s")

            return result

        return inner

    return mean_time


@mean_deco(10)
def foo(arg1):
    sleep(random())
    return 10


@mean_deco(2)
def boo(a, b):
    return a + b


if __name__ == "__main__":
    for _ in range(30):
        foo("Walter")
