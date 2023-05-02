from weakref import ref
from time import time
from cProfile import Profile
from pstats import Stats
from memory_profiler import profile


class Model:
    def __init__(self, value):
        self.value = value


class EngineSize:
    def __init__(self, value):
        self.value = value


class Price:
    def __init__(self, value):
        self.value = value


class Car:
    def __init__(self, model, eng_size, price):
        self.model = Model(model)
        self.eng_size = EngineSize(eng_size)
        self.price = Price(price)


class CarSlots:
    __slots__ = ("model", "eng_size", "price")

    def __init__(self, model, eng_size, price):
        self.model = Model(model)
        self.eng_size = EngineSize(eng_size)
        self.price = Price(price)


class CarWeakRef:
    def __init__(self, model, eng_size, price):
        self.model = ref(Model(model))
        self.eng_size = ref(EngineSize(eng_size))
        self.price = ref(Price(price))


def attr_access_time(cars):
    start = time()

    new_model = Model("BMW 320d")
    new_eng_size = EngineSize(2.0)
    new_price = Price(60000)

    for car in cars:
        model = car.model
        eng_size = car.eng_size
        price = car.price
        car.model = new_model
        car.eng_size = new_eng_size
        car.price = new_price

    end = time()
    return end - start


@profile
def measure_time(N):
    start = time()
    cars = [Car("Audi A6", 3.0, 45000) for _ in range(N)]
    end = time()
    default_time = end - start

    start = time()
    cars_slots = [CarSlots("Audi A6", 3.0, 45000) for _ in range(N)]
    end = time()
    slots_time = end - start

    start = time()
    cars_weakref = [CarWeakRef("Audi A6", 3.0, 45000) for _ in range(N)]
    end = time()
    weakref_time = end - start

    default_attr_time = attr_access_time(cars)
    slots_attr_time = attr_access_time(cars_slots)
    weakref_attr_time = attr_access_time(cars_weakref)

    print(f'Default Init Time: {default_time}')
    print(f'Slots Init Time: {slots_time}')
    print(f'WeakRef Init Time: {weakref_time}\n')

    print(f'Default Attr Access Time: {default_attr_time}')
    print(f'Slots Attr Access Time: {slots_attr_time}')
    print(f'WeakRef Attr Access Time: {weakref_attr_time}')


if __name__ == "__main__":
    N = 500_000
    pr = Profile()

    pr.enable()
    measure_time(N)
    pr.disable()

    ps = Stats(pr).strip_dirs().sort_stats("cumulative")
    ps.print_stats()
