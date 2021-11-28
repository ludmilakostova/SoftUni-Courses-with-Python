from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
        else:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f'Successfully added {aquarium_type}.'

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Plant":
            deco = Plant()
        elif decoration_type == "Ornament":
            deco = Ornament()
        else:
            return "Invalid decoration type."
        self.decorations_repository.add(deco)
        return f'Successfully added {decoration_type}.'

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        deco = self.decorations_repository.find_by_type(decoration_type)
        if deco == "None":
            return f'There isn\'t a decoration of type {decoration_type}.'
        else:
            try:
                aqua = [aquarium for aquarium in self.aquariums if aquarium.name == aquarium_name][0]
                aqua.add_decoration(deco)
                self.decorations_repository.remove(deco)
                return f'Successfully added {decoration_type} to {aquarium_name}.'
            except IndexError:
                pass

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        elif fish_type == "SaltwaterFish":
            fish = SaltwaterFish(fish_name, fish_species, price)
        else:
            return f'There isn\'t a fish of type {fish_type}.'

        # try:
        aqua_obj = [a for a in self.aquariums if a.name == aquarium_name][0]
        return aqua_obj.add_fish(fish)
        # except IndexError:
        #     pass

    def feed_fish(self, aquarium_name: str):
        try:
            aqua_obj = [a for a in self.aquariums if aquarium_name == a.name][0]
            aqua_obj.feed()
            return f'Fish fed: {len(aqua_obj.fish)}'
        except IndexError:
            pass

    def calculate_value(self, aquarium_name: str):
        aqua_obj = [a for a in self.aquariums if aquarium_name == a.name][0]
        fish_prices = sum([f.price for f in aqua_obj.fish])
        deco_prices = sum([deco.price for deco in aqua_obj.decorations])
        result = fish_prices + deco_prices
        return f'The value of Aquarium {aquarium_name} is {result:.2f}.'

    def report(self):
        result = ""
        for aquarium in self.aquariums:
            result += str(aquarium)
            result += f'\n'
        return result.strip()
