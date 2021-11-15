from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        power_hardware_object = PowerHardware(name, capacity, memory)
        System._hardware.append(power_hardware_object)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        obj_heavy_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(obj_heavy_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for obj in System._hardware:
            if obj.name == hardware_name:
                express_software_object = ExpressSoftware(name, capacity_consumption, memory_consumption)
                try:
                    obj.install(express_software_object)
                except Exception:
                    return "Software cannot be installed"
                System._software.append(express_software_object)
                return
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for obj in System._hardware:
            if obj.name == hardware_name:
                light_software_object = LightSoftware(name, capacity_consumption, memory_consumption)
                try:
                    obj.install(light_software_object)
                except Exception:
                    return "Software cannot be installed"
                System._software.append(light_software_object)
                return
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hard_obj = [h for h in System._hardware if h.name == hardware_name][0]
        software_obj = [s for s in System._software if s.name == software_name][0]
        if hard_obj and software_obj:
            hard_obj.uninstall(software_obj)
            System._software.remove(software_obj)
        else:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = ""
        result += f'System Analysis\n'
        result += f'Hardware Components: {len(System._hardware)}\nSoftware Components: {len(System._software)}\n'
        total_soft_memory = sum([obj.memory_consumption for obj in System._software])
        total_hard_memory = sum([obj.memory for obj in System._hardware])
        result += f'Total Operational Memory: {total_soft_memory} / {total_hard_memory}\n'
        total_soft_capacity = sum([s.capacity_consumption for s in System._software])
        total_hard_capacity = sum([h.capacity for h in System._hardware])
        result += f'Total Capacity Taken: {total_soft_capacity} / {total_hard_capacity}'
        return result

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f'Hardware Component - {h.name}\n'
            count_soft_exp = 0
            count_soft_light = 0
            memory_used = 0
            capacity_used = 0
            soft_name = []
            for soft in h.software_components:
                if isinstance(soft, ExpressSoftware):
                    count_soft_exp += 1
                elif isinstance(soft, LightSoftware):
                    count_soft_light += 1
                memory_used += soft.memory_consumption
                capacity_used += soft.capacity_consumption
                soft_name.append(soft.name)
            result += f'Express Software Components: {count_soft_exp}\n'
            result += f'Light Software Components: {count_soft_light}\n'
            result += f'Memory Usage: {memory_used} / {h.memory}\n'
            result += f'Capacity Usage: {capacity_used} / {h.capacity}\n'
            result += f'Type: {h.hardware_type}\n'
            result += f'Software Components: {", ".join(soft_name) if soft_name else "None"}\n'
        return result.strip()



