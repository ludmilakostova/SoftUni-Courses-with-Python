from abc import ABC, abstractmethod


class BaseFish(ABC):
    @abstractmethod
    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = str(name)
        self.species = str(species)
        self.size = int(size)
        self.price = float(price)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Fish name cannot be an empty string.")
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        if value == "" or value == " ":
            raise ValueError("Fish species cannot be an empty string.")
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError('Price cannot be equal to or below zero.')
        self.__price = value

    def eat(self):
        self.size += 5

