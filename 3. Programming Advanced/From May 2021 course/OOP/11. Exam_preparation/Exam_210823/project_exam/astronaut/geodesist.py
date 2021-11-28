from project_exam.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    LOST_OXYGEN_PER_BREATH = 10

    def __init__(self, name: str):
        super().__init__(name, 50)

    def breathe(self):
        self.oxygen -= Geodesist.LOST_OXYGEN_PER_BREATH

