from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        result_exp = sum([room.expenses for room in self.rooms])
        result_cost = sum([r.room_cost for r in self.rooms])
        total_consumption = result_exp + result_cost
        return f'Monthly consumptions: {total_consumption:.2f}$.'

    def pay(self):
        result = []
        for room in self.rooms:
            total_consumption = room.expenses + room.room_cost
            if room.budget >= total_consumption:
                room.budget -= total_consumption
                result.append(f'{room.family_name} paid {total_consumption:.2f}$ and have {room.budget:.2f}$ left.')
            else:
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")
                self.rooms.remove(room)
        return "\n".join(result)

    def status(self):
        result = ""
        total_population = sum([room.members_count for room in self.rooms])
        result += f"Total population: {total_population}\n"
        for room in self.rooms:
            result += f'{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, Expenses: {room.expenses:.2f}$\n'
            if room.children:
                for i in range(len(room.children)):
                    result += f"--- Child {i + 1} monthly cost: {(room.children[i].cost * 30):.2f}$\n"
            if hasattr(room, 'appliances'):
                app_expenses = 0
                for a in room.appliances:
                    app_expenses += a.get_monthly_expense()
                result += f"--- Appliances monthly cost: {app_expenses:.2f}$\n"
        return result



