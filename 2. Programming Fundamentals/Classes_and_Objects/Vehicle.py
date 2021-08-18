class Vehicle:
    def __init__(self, type: str, model: str, price: int):
        self.type = type
        self.model = model
        self.price = price
        self.owner = "None"

    def buy(self, money, owner):
        if self.owner != "None":
            result = "Car already sold"
        if self.price <= money and self.owner:
            self.owner = owner
            result = f"Successfully bought a {self.type}. Change: {money - self.price:.2f}"
        else:
            result = "Sorry, not enough money"

        return result

    def sell(self):
        if self.owner != "None":
            self.owner = "None"
        else:
            return "Vehicle has no owner"

    def __repr__(self):
        if self.owner == "None":
            result = f'{self.model} {self.type} is on sale: {self.price}'
        else:
            result = f'{self.model} {self.type} is owned by: {self.owner}'
        return result


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)





