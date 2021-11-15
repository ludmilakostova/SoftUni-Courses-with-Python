from project.hardware.hardware import Hardware
import math


class HeavyHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Heavy", 2*capacity, math.floor(0.75*memory))
