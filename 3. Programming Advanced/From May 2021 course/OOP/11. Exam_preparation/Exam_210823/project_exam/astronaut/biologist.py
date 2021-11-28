from project_exam.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    LOST_OXYGEN_PER_BREATH: int = 5

    def __init__(self, name: str):
        super().__init__(name, 70)

    def breathe(self):
        self.oxygen -= Biologist.LOST_OXYGEN_PER_BREATH


