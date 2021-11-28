from project_exam.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    LOST_OXYGEN_PER_BREATH = 15

    def __init__(self, name: str):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= Meteorologist.LOST_OXYGEN_PER_BREATH

