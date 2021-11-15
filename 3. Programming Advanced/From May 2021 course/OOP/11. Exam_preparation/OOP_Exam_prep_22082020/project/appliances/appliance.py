class Appliance:
    def __init__(self, cost: float):
        self.cost = cost

    def get_monthly_expense(self):
        result = self.cost * 30
        return result

