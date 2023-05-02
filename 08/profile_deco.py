from cProfile import Profile
from pstats import Stats


def profile_deco(func):
    def wrapper(*args, **kwargs):
        if "pr" not in wrapper.__dict__.keys():
            wrapper.pr = Profile()

        result = wrapper.pr.runcall(func, *args, **kwargs)

        def print_stat():
            st = Stats(wrapper.pr).strip_dirs().sort_stats("cumulative")
            st.print_stats()

        wrapper.print_stat = print_stat
        return result
    return wrapper


@profile_deco
def add(a, b):
    return a + b


@profile_deco
def sub(a, b):
    return a - b


if __name__ == "__main__":
    for i in range(52):
        sub(31, 314)
    for _ in range(116):
        add(233, -17)
    add.print_stat()
    sub.print_stat()
