from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = str(name)
        self.capacity = int(capacity)
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError('Aquarium name cannot be an empty string.')
        self.__name = value

    @property
    def available_capacity(self):
        return self.capacity - len(self.fish)

    def calculate_comfort(self):
        result = sum([d.comfort for d in self.decorations])
        return result

    def add_fish(self, fish):
        if self.available_capacity <= 0:
            return f'Not enough capacity.'
        self.fish.append(fish)
        return f'Successfully added {fish.__class__.__name__} to {self.name}.'

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = ""
        result += f'{self.name}:\n'
        if self.fish:
            result += f'Fish: {" ".join([f.name for f in self.fish])}\n'
        else:
            result += f'Fish: none\n'
        result += f'Decorations: {len(self.decorations)}\n'
        result += f'Comfort: {self.calculate_comfort()}'
        return result.strip()




