class Subscription:
    __count = 1

    def __init__(self, date:str, customer_id: int, trainer_id: int, exercise_id: int):
        self.date = str(date)
        self.customer_id = int(customer_id)
        self.trainer_id = int(trainer_id)
        self.exercise_id = int(exercise_id)
        self.id = __class__.__count
        __class__.__count += 1

    @staticmethod
    def get_next_id():
        return __class__.__count

    def __repr__(self):
        return f'Subscription <{self.id}> on {self.date}'
