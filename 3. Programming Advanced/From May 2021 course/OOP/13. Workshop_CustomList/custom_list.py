from copy import deepcopy


class CustomList:
    def __init__(self, *args):
        self.__values = list(args)

    def append(self, value):
        self.__values.append(value)

    def remove(self, index):
        if 0 <= index < len(self.__values):
            result = self.__values.pop(index)
            return result
        else:
            raise IndexError("Invalid index")

    def get(self, index):
        try:
            el = self.__values[index]
            return el
        except IndexError:
            raise IndexError("Invalid index")

    def extend(self, object):
        try:
            iter(object)
            self.__values.extend(object)
        except TypeError:
            self.__values.append(object)

        return deepcopy(self.__values)

    def insert(self, index, value):
        if index >= len(self.__values) or index < 0:
            raise IndexError("Invalid index")
        self.__values.insert(index, value)
        return self.__values

    def pop(self):
        try:
            el = self.__values.pop()
            return el
        except IndexError:
            raise IndexError("Empty List")

    def clear(self):
        self.__values = []

    def index(self, value):
        try:
            return self.__values.index(value)
        except ValueError:
            raise ValueError("Nonexistent value")

    def reverse(self):
        result = list(reversed(self.__values))
        return result

    def copy(self):
        return deepcopy(self.__values)

    def size(self):
        return len(self.__values)

    def add_first(self, value):
        return self.__values.insert(0, value)

    def dictionize(self):
        result = {}
        for i in range(len(self.__values)):
            if i % 2 == 0:
                if i == len(self.__values) - 1:
                    break
                else:
                    result[self.__values[i]] = self.__values[i + 1]
        if len(self.__values) % 2 == 1:
            result[self.__values[-1]] = " "
        return result

    def move(self, amount):
        result = []
        if amount <= len(self.__values):
            result = self.__values[amount:] + self.__values[:amount]
            return result
        return "Amount to big - list unchanged"

    def sum(self):
        res = 0
        for el in self.__values:
            if isinstance(el, int):
                res += el
            else:
                res += len(el)
        return res




