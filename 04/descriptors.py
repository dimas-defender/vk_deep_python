class String:
    def __set_name__(self, owner, name):
        self._instance_attr_name = f"_str_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            raise TypeError("Object is None!")

        return getattr(obj, self._instance_attr_name)

    def __set__(self, obj, val):
        if obj is None:
            raise TypeError("Object is None!")

        if not isinstance(val, str):
            raise TypeError("Wrong type!")

        if len(val) < 3 or val[0].islower():
            raise ValueError("Wrong value!")

        return setattr(obj, self._instance_attr_name, val)

    def __delete__(self, obj):
        if obj is None:
            raise TypeError("Object is None!")

        return delattr(obj, self._instance_attr_name)


class Year:
    def __set_name__(self, owner, name):
        self._instance_attr_name = f"_year_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            raise TypeError("Object is None!")

        return getattr(obj, self._instance_attr_name)

    def __set__(self, obj, val):
        if obj is None:
            raise TypeError("Object is None!")

        if not isinstance(val, int):
            raise TypeError("Wrong type!")

        if val < 1900 or val > 2023:
            raise ValueError("Wrong value!")

        return setattr(obj, self._instance_attr_name, val)

    def __delete__(self, obj):
        if obj is None:
            raise TypeError("Object is None!")

        return delattr(obj, self._instance_attr_name)


class LimitedFloat:
    def __set_name__(self, owner, name):
        self._instance_attr_name = f"_limfloat_{name}"

    def __get__(self, obj, objtype):
        if obj is None:
            raise TypeError("Object is None!")

        return getattr(obj, self._instance_attr_name)

    def __set__(self, obj, val):
        if obj is None:
            raise TypeError("Object is None!")

        if not isinstance(val, float):
            raise TypeError("Wrong type!")

        if val < 0.5 or val > 6.0:
            raise ValueError("Wrong value!")

        return setattr(obj, self._instance_attr_name, val)

    def __delete__(self, obj):
        if obj is None:
            raise TypeError("Object is None!")

        return delattr(obj, self._instance_attr_name)


class Car:
    model = String()
    manufactured = Year()
    engine_size = LimitedFloat()

    def __init__(self, model, year, size):
        self.model = model
        self.manufactured = year
        self.engine_size = size
