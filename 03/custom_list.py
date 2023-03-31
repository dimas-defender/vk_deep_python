class CustomList(list):
    def __init__(self, items):
        super().__init__(item for item in items if type(item) in [int, float])

    def __add__(self, other):
        len_max = len(self)
        len_min = len(other)
        swap_flag = False

        if len_max < len_min:
            len_max, len_min = len_min, len_max
            swap_flag = True

        result = [0] * len_min
        for i in range(len_min):
            result[i] = self[i] + other[i]

        if len_max > len_min:
            result.extend(other[len_min:] if swap_flag else self[len_min:])
        return CustomList(result)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        len_max = len(self)
        len_min = len(other)
        swap_flag = False

        if len_max < len_min:
            len_max, len_min = len_min, len_max
            swap_flag = True

        result = [0] * len_min
        for i in range(len_min):
            result[i] = self[i] - other[i]

        if len_max > len_min:
            result.extend([-x for x in other[len_min:]] if swap_flag
                          else self[len_min:])
        return CustomList(result)

    def __rsub__(self, other):
        temp = self - other
        return CustomList([-x for x in temp])

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __str__(self):
        return f"Items: {list(self)} Sum: {sum(self)}"
