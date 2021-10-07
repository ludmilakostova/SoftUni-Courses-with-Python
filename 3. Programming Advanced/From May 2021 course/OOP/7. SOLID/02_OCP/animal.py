from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def get_sound(self):
        pass


class Cat(Animal):
    def get_sound(self):
        return "Meow"


class Dog(Animal):
    def get_sound(self):
        return "woof-woof"


def animal_sound(animals: list):
    for animal in animals:
        print(animal.get_sound())


animals = [Cat(), Dog()]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
