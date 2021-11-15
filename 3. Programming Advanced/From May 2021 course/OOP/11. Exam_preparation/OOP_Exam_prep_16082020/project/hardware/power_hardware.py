from project.hardware.hardware import Hardware
import math


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", math.floor(0.25*capacity), math.floor(1.75*memory))




