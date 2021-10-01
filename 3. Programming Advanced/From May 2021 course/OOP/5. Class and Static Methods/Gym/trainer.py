class Trainer:
    __count = 1

    def __init__(self, name: str):
        self.name = str(name)
        self.id = __class__.__count
        __class__.__count += 1

    @staticmethod
    def get_next_id():
        return __class__.__count

    def __repr__(self):
        return f'Trainer <{self.id}> {self.name}'
