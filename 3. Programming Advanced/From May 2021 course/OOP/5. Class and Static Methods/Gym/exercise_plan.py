class ExercisePlan:
    __counter = 1

    def __init__(self, trainer_id: int, equipment_id: int, duration: int):
        self.trainer_id = int(trainer_id)
        self.equipment_id = int(equipment_id)
        self.duration = int(duration)
        self.id = __class__.__counter
        __class__.__counter += 1

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(int(trainer_id), int(equipment_id), int(hours) * 60)

    @staticmethod
    def get_next_id():
        return __class__.__counter

    def __repr__(self):
        return f'Plan <{self.id}> with duration {self.duration} minutes'

