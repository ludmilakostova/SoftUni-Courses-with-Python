class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer) -> bool:
        if len(self.customers) < self.customer_capacity():
            self.customers.append(customer)
            return True
        return False

    def add_dvd(self, dvd) -> bool:
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)
            return True
        return False

    def rent_dvd(self, customer_id: int, dvd_id: int):
        dvd_object = [dvd for dvd in self.dvds if dvd_id == dvd.id][0]
        cl_object = [c for c in self.customers if c.id == customer_id][0]
        if dvd_id in [d.id for d in cl_object.rented_dvds]:
            return f'{cl_object.name} has already rented {dvd_object.name}'
        if cl_object.age < dvd_object.age_restriction:
            return f"{cl_object.name} should be at least {dvd_object.age_restriction} to rent this movie"
        if dvd_object.is_rented:
            return 'DVD is already rented'
        dvd_object.is_rented = True
        cl_object.rented_dvds.append(dvd_object)
        return f"{cl_object.name} has successfully rented {dvd_object.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = [d for d in self.dvds if dvd_id == d.id][0]
        customer = [c for c in self.customers if customer_id == c.id][0]

        if dvd_id in [d.id for d in customer.rented_dvds]:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f'{customer.name} has successfully returned {dvd.name}'
        return f'{customer.name} does not have that DVD'

    def __repr__(self):
        result = ""
        customers = "\n".join([c.__repr__() for c in self.customers]) + "\n"
        dvds = "\n".join([d.__repr__() for d in self.dvds])
        result += customers
        result += dvds
        return result







