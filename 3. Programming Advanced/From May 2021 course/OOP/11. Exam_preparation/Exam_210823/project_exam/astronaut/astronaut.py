from abc import ABC, abstractmethod


class Astronaut(ABC):
    LOST_OXYGEN_PER_BREATH = 10

    def __init__(self, name: str, oxygen: int):
        self.name = str(name)
        self.oxygen = int(oxygen)
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= __class__.LOST_OXYGEN_PER_BREATH

    def increase_oxygen(self, amount: int):
        self.oxygen += amount



