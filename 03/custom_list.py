

class CustomList(list):
    def __init__(self, items):
        super().__init__(item for item in items if type(item) in [int, float])
        #self.data = [item for item in items if type(item) in [int, float]]

    def __add__(self, other):
        N_max = len(self)
        N_min = len(other)
        swap_flag = False

        if N_max < N_min:
            N_max, N_min = N_min, N_max
            swap_flag = True 

        result = [0] * N_min
        for i in range(N_min):
            result[i] = self[i] + other[i]

        if N_max > N_min:
            result.extend(other[N_min:] if swap_flag else self[N_min:])
        return CustomList(result)
    
    
    def __radd__(self, other):
        return self + other
    
    
    def __sub__(self, other):
        N_max = len(self)
        N_min = len(other)
        swap_flag = False

        if N_max < N_min:
            N_max, N_min = N_min, N_max
            swap_flag = True 

        result = [0] * N_min
        for i in range(N_min):
            result[i] = self[i] + other[i]

        if N_max > N_min:
            result.extend(other[N_min:] if swap_flag else self[N_min:])
        return CustomList(result)
    
    
    def __rsub__(self, other):
        return self + other
    
    def __eq__(self, other):
        return sum(self.data) == sum(other.data)
    
    def __ne__(self, other):
        return sum(self.data) != sum(other.data)

    def __gt__(self, other):
        return sum(self) > sum(other)
    
    def __ge__(self, other):
        return sum(self.data) >= sum(other.data)
    
    def __lt__(self, other):
        return sum(self.data) < sum(other.data)
    
    def __le__(self, other):
        return sum(self.data) <= sum(other.data)
    
    def __str__(self):
        return f"Items: {[x for x in self]}\nSum: {sum(self)}"


print(CustomList([5, 1, 3, 7]) + CustomList([1, 2, 7]))  # CustomList([6, 3, 10, 7])
print(CustomList([1]) + [2, 5])  # CustomList([3, 5])
print([2, 5] + CustomList([1]))  # CustomList([3, 5])

print(CustomList([5, 1, 3, 7]) - CustomList([1, 2, 7]))  # CustomList([4, -1, -4, 7])
print(CustomList([1]) - [2, 5])  # CustomList([-1, -5])
print([2, 5] - CustomList([1]))  # CustomList([1, 5])
