from project_exam.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)
            return True
        return False

    def find_by_name(self, name: str):
        planet = [p for p in self.planets if p.name == name]
        if planet:
            return planet[0]
