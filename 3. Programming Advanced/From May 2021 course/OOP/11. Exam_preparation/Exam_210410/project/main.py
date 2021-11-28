from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.controller import Controller
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish

o = Ornament()
p = Plant()
d = DecorationRepository()
d.add(o)
d.add(p)
print(d.find_by_type("Plant"))
fresh_fish = FreshwaterFish("Io", "blue", 100)
fresh_fish.eat()
print(fresh_fish.size)
saltwater_fish = SaltwaterFish("Bi", "red", 100)
saltwater_fish.eat()
print(saltwater_fish.size)
fresh_aquarium = FreshwaterAquarium("FreshWater")
saltwater_aquarium = SaltwaterAquarium("Saltwater")
print(fresh_aquarium.available_capacity)
print(saltwater_aquarium.available_capacity)
controller = Controller()
print(controller.add_aquarium("FreshwaterAquarium", "Mila"))
print(controller.aquariums)
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Plant"))
print(controller.add_decoration("Ornament"))
print(controller.decorations_repository.decorations)
print(controller.insert_decoration("Mila", "Plant"))
print(controller.decorations_repository.decorations)
print(controller.add_aquarium("SaltwaterAquarium", "Goran"))
print(controller.report())
print(controller.add_fish("Goran", "SaltwaterFish", "Lu", "Black", 120))
print(controller.add_fish("Goran", "SaltwaterFish", "Ul", "Black", 120))
print(controller.feed_fish("Goran"))
print(controller.calculate_value("Goran"))
print(controller.insert_decoration("Pui", "Plant"))
print(controller.decorations_repository.decorations)
print(controller.add_decoration("Plant"))
print(controller.decorations_repository.decorations)