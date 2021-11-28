from copy import deepcopy


class HashTable:
    """A class representing..."""

    def __init__(self):
        self.max_capacity = 4
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def __setitem__(self, key, value):
        """Try to see if the key is already in the list. If it is not, we find the new index and set it
        up. If it does, we change the value"""
        if len([el for el in self.__keys if el is not None]) == self.max_capacity:
            self.__resize()

        try:
            index = self.__keys.index(key)
            self.__values[index] = value
            return
        except ValueError:
            index = self.get_available_index(key)
            self.__keys[index] = key
            self.__values[index] = value

    def __resize(self):
        self.__keys = self.__keys + [None] * self.max_capacity
        self.__values = self.__values + [None] * self.max_capacity
        self.max_capacity *= 2

    def __getitem__(self, key):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key is not in dict")

    def __check_index(self, index):
        if index == len(self.__keys):
            return self.__check_index(0)
        if self.__keys[index] is None:
            return index
        return self.__check_index(index + 1)

    def get_available_index(self, key):
        """

        :param key:
        :return:
        """
        index = self.hash(key)
        available_index = self.__check_index(index)
        return available_index

    def hash(self, key):
        index = sum([ord(char) for char in key]) % self.max_capacity
        return index

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    def __len__(self):
        return len([el for el in self.__keys if el is not None])

    def keys(self):
        return [el for el in self.__keys if el is not None]

    def values(self):
        keys = self.keys()
        value_list = []
        for key in keys:
            index = self.__keys.index(key)
            value_list.append(self.__values[index])
        return value_list

    def items(self):
        return list(zip(self.keys(), self.values()))

    def clear(self):
        self.__keys = [None] * self.max_capacity
        self.__values = [None] * self.max_capacity

    def copy(self):
        return deepcopy(self)

    def pop(self, key):
        try:
            index = self.__keys.index(key)
            self.__keys[index] = None
            el = self.__values[index]
            self.__values[index] = None
            return el
        except ValueError:
            raise KeyError("Key is not in dict")

    def __repr__(self):
        to_str = []
        for key, value in self.items():
            to_str.append(f"{key}:{value}")
        return "{" + ", ".join(to_str) + "}"


table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
print(table.keys())
print(table.values())
print(table.items())
# table.clear()
print(table)
a = table.copy()
a["name"] = 6
print(a["name"])
print(table["name"])
print(table)

