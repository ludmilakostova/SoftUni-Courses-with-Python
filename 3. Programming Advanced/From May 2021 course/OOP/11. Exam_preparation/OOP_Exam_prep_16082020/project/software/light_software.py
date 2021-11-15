from project.software.software import Software
import math


class LightSoftware(Software):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Light", math.floor(capacity * 1.5), math.floor(memory/2))



