from project_exam.astronaut.astronaut_repository import AstronautRepository
from project_exam.astronaut.biologist import Biologist
from project_exam.astronaut.geodesist import Geodesist
from project_exam.astronaut.meteorologist import Meteorologist
from project_exam.planet.planet import Planet
from project_exam.planet.planet_repository import PlanetRepository


class SpaceStation:
    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type == "Biologist":
            astro = Biologist(name)
        elif astronaut_type == "Geodesist":
            astro = Geodesist(name)
        elif astronaut_type == "Meteorologist":
            astro = Meteorologist(name)
        else:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'
        self.astronaut_repository.add(astro)
        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'
        planet = Planet(name)
        items_list = items.split(", ")
        for item in items_list:
            planet.items.append(item)
        self.planet_repository.add(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astro = self.astronaut_repository.find_by_name(name)
        if astro:
            self.astronaut_repository.remove(astro)
            return f'Astronaut {name} was retired!'
        else:
            raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astro in self.astronaut_repository.astronauts:
            astro.oxygen += 10

    def send_on_mission(self, planet_name: str):
        if not self.planet_repository.find_by_name(planet_name):
            raise Exception("Invalid planet name!")

        location = self.planet_repository.find_by_name(planet_name)
        astro_oxy = [a_obj for a_obj in self.astronaut_repository.astronauts if a_obj.oxygen > 30]
        if not astro_oxy:
            raise Exception("You need at least one astronaut to explore the planet!")
        astro_oxy.sort(key=lambda x: x.oxygen, reverse=True)
        while len(astro_oxy) > 5:
            astro_oxy.pop(-1)
        count_astro = 0
        for astro in astro_oxy:
            count_astro += 1
            while location.items:
                astro.backpack.append(location.items.pop())
                astro.breathe()
                if astro.oxygen <= 0:
                    break
            if not location.items:
                break

        if not location.items:
            return f'Planet: {planet_name} was explored. {count_astro} astronauts participated in collecting items.'
        return f'Mission is not completed.'

    def report(self):
        result = ""
        successful_mission = 0
        unsuccessful_mission = 0
        for planet in self.planet_repository.planets:
            if planet.items:
                unsuccessful_mission += 1
            else:
                successful_mission += 1
        result += f'{successful_mission} successful missions!\n{unsuccessful_mission} missions were not completed!\n'
        result += f'Astronauts\' info:\n'
        for astro in self.astronaut_repository.astronauts:
            result += f'Name: {astro.name}\n'
            result += f'Oxygen: {astro.oxygen}\n'
            result += f'Backpack items: {", ".join(astro.backpack)if astro.backpack else "none"}\n'
        return result.strip()


space_station = SpaceStation()
print(space_station.add_astronaut("Meteorologist", "Mila"))
print(space_station.add_astronaut("Meteorologist", "Mila"))
print(space_station.add_astronaut("Geodesist", "Petar"))
print(space_station.add_astronaut("Biologist", "Viktor"))
print(space_station.add_astronaut("Biologist", "Goran"))
print(space_station.add_planet("Lulu", "Bijou, travail, choucou"))
print(space_station.add_planet("Lulu", "Bijou, travail, choucou"))
# print(space_station.retire_astronaut("Viktor"))
print(space_station.recharge_oxygen())
for a in space_station.astronaut_repository.astronauts:
    print(a.oxygen)
print(space_station.send_on_mission("Lulu"))
print(space_station.report())
