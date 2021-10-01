class Customer:
    id: int = 1

    def __init__(self, name: str, address: str, email: str):
        self.name = str(name)
        self.address = str(address)
        self.email = str(email)
        self.id = __class__.id
        __class__.id += 1

    @staticmethod
    def get_next_id():
        return __class__.id

    def __repr__(self):
        return f'Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}'













