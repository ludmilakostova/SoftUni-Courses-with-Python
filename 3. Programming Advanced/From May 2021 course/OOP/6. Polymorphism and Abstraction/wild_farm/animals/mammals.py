from wild_farm.animals.animal import Mammal
from wild_farm.food import Fruit, Vegetable, Meat


class Mouse(Mammal):
    def __init__(self, name: str, weight, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Fruit, Vegetable]
        self.weight_per_food = 0.1

    def make_sound(self):
        return "Squeak"

    # def feed(self, food):
    #     if not isinstance(food, Fruit) or not isinstance(food, Vegetable):
    #         return f"{type(self).__name__} does not eat {food.__class__.__name__}!"
    #     self.weight += 0.10 * food.quantity
    #     self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name: str, weight, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.4

    def make_sound(self):
        return "Woof!"

    # def feed(self, food):
    #     if isinstance(food, Meat):
    #         self.weight += 0.40 * food.quantity
    #         self.food_eaten += food.quantity
    #         return
    #     return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Cat(Mammal):
    def __init__(self, name: str, weight, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat, Vegetable]
        self.weight_per_food = 0.3

    def make_sound(self):
        return "Meow"

    # def feed(self, food):
    #     if isinstance(food, Vegetable) or isinstance(food, Meat):
    #         self.weight += 0.30 * food.quantity
    #         self.food_eaten += food.quantity
    #         return
    #     return f'{self.__class__.__name__} does not eat {type(food).__name__}!"'


class Tiger(Mammal):
    def __init__(self, name: str, weight, living_region: str):
        super().__init__(name, weight, living_region)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 1

    def make_sound(self):
        return "ROAR!!!"

    # def feed(self, food):
    #     if isinstance(food, Meat):
    #         self.weight += 1.00 * food.quantity
    #         self.food_eaten += food.quantity
    #         return
    #     return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'
