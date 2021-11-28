from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = str(name)
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "" or value == " ":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type == "Bread":
            food = Bread(name, price)
        elif food_type == "Cake":
            food = Cake(name, price)

        searched_food = [f for f in self.food_menu if food.name == f.name]
        if searched_food:
            raise Exception(f'{food_type} {name} is already in the menu!')
        else:
            self.food_menu.append(food)
            return f'Added {food.name} ({food.__class__.__name__}) to the food menu'

    def add_drink(self, drink_type: str, name: str, portion: int, brand: str):
        if drink_type == "Water":
            drink_obj = Water(name, portion, brand)
        elif drink_type == "Tea":
            drink_obj = Tea(name, portion, brand)

        searched_drink = [d for d in self.drinks_menu if d.name == drink_obj.name]
        if searched_drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")
        else:
            self.drinks_menu.append(drink_obj)
            return f'Added {name} ({brand}) to the drink menu'

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type == "InsideTable":
            table = InsideTable(table_number, capacity)
        elif table_type == "OutsideTable":
            table = OutsideTable(table_number, capacity)

        searched_table = [t for t in self.tables_repository if t.table_number == table_number]
        if searched_table:
            raise Exception(f'Table {table_number} is already in the bakery!')
        else:
            self.tables_repository.append(table)
            return f'Added table number {table_number} in the bakery'

    def reserve_table(self, number_of_people: int):
        try:
            table = [t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people][0]
            table.reserve(number_of_people)
            return f'Table {table.table_number} has been reserved for {number_of_people} people'
        except IndexError:
            return f'No available table for {number_of_people} people'

    def order_food(self, table_number: int, *args):
        try:
            table = [t for t in self.tables_repository if t.table_number == table_number][0]
            food_not_found = []
            for food_name in args:
                if food_name in [f.name for f in self.food_menu]:
                    food_obj = [f for f in self.food_menu if f.name == food_name][0]
                    table.food_orders.append(food_obj)
                else:
                    food_not_found.append(food_name)

            result = ''
            if table.food_orders:
                result += f'Table {table_number} ordered:\n'
                for f in table.food_orders:
                    result += f'{repr(f)}\n'
            if food_not_found:
                result += f'{self.name} does not have in the menu:\n'
                result += '\n'.join(food_not_found)
            return result
        except IndexError:
            return f'Could not find table {table_number}'

    def order_drink(self, table_number: int, *args):
        try:
            table = [t for t in self.tables_repository if t.table_number == table_number][0]
        except IndexError:
            return f'Could not find table {table_number}'

        drinks_not_in_menu = []
        for drink_name in args:
            if drink_name in [d.name for d in self.drinks_menu]:
                drink_obj = [d for d in self.drinks_menu if drink_name == d.name][0]
                table.drink_orders.append(drink_obj)
            else:
                drinks_not_in_menu.append(drink_name)

        result = ""
        if table.drink_orders:
            result += f'Table {table_number} ordered:\n'
            for d in table.drink_orders:
                result += f'{repr(d)}\n'
        if drinks_not_in_menu:
            result += f'{self.name} does not have in the menu:\n'
            result += "\n".join(drinks_not_in_menu)
        return result

    def leave_table(self, table_number: int):
        current_bill = 0
        try:
            table = [t for t in self.tables_repository if t.table_number == table_number][0]
            current_bill += table.get_bill()
            self.total_income += current_bill
            table.clear()
            return f'Table: {table_number}\nBill: {current_bill:.2f}'
        except IndexError:
            pass

    def get_free_tables_info(self):
        result = ""
        for table in self.tables_repository:
            if not table.is_reserved:
                result += f'{table.free_table_info()}\n'
        return result

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}lv'


# tea = Tea("Lulu", 100, "Mila")
# water = Water("Mila", 150, "Coucou")
# bakery = Bakery("Mila")
# bakery.add_drink("Water", "Mila", 50, "hjg")
# print(bakery.add_table("InsideTable", 4, 20))
# print(bakery.add_table("OutsideTable", 55, 50))
# print(bakery.add_table("InsideTable", 25, 60))
# print(bakery.reserve_table(25))
# baked_food = Bread("Ko", 2)
# cake_food = Cake("Lo", 15)
# bakery.add_food("Bread", "Ko", 6)
# bakery.add_food("Cake", "Lo", 2)
# print(bakery.order_food(4, "pasta", "Ko", "Lo", "poulet"))
# print(bakery.order_drink(6, "Mila", "Ko", "Lo", "poulet"))
# print(bakery.leave_table(4))
# print(bakery.get_free_tables_info())
# print(bakery.get_total_income())
