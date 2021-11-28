from project_exam.astronaut.astronaut_repository import AstronautRepository
from project_exam.astronaut.biologist import Biologist
from project_exam.astronaut.geodesist import Geodesist
from project_exam.astronaut.meteorologist import Meteorologist

b = Biologist("Kate")
c = Geodesist("Pat")
d = Meteorologist("Pu")
astro_repo = AstronautRepository()
astro_repo.add(b)
astro_repo.add(c)
astro_repo.add(d)
print(astro_repo.find_by_name("Kate"))
print(astro_repo.astronauts)
d.breath()
print(d.oxygen)
