from wild_farm.animals.animal import Bird, Animal
from wild_farm.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.acceptable_foods = [Meat]
        self.weight_per_food = 0.25

    def make_sound(self):
        return "Hoot Hoot"

    # def feed(self, food):
    #     if isinstance(food, Meat):
    #         self.weight += 0.25 * food.quantity
    #         self.food_eaten += food.quantity
    #         return
    #     return f'{self.__class__.__name__} does not eat {food.__class__.__name__}!'


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size):
        super().__init__(name, weight, wing_size)
        self.acceptable_foods = [Meat, Vegetable, Fruit, Seed]
        self.weight_per_food = 0.35

    def make_sound(self):
        return "Cluck"

    # def feed(self, food):
    #     self.weight += 0.35 * food.quantity
    #     self.food_eaten += food.quantity


owl = Owl("Pip", 10, 10)
print(owl)
meat = Meat(4)
print(owl.make_sound())
owl.feed(meat)
veg = Vegetable(1)
print(owl.feed(veg))
print(owl)
hen = Hen("Harry", 10, 10)
veg = Vegetable(3)
fruit = Fruit(5)
meat = Meat(1)
print(hen)
print(hen.make_sound())
hen.feed(veg)
hen.feed(fruit)
hen.feed(meat)
print(hen)






