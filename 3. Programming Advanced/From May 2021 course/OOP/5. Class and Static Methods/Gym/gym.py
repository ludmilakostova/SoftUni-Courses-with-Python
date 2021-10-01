from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, client: Customer):
        if client not in self.customers:
            self.customers.append(client)
        return False

    def add_trainer(self, coach: Trainer):
        if coach not in self.trainers:
            self.trainers.append(coach)
        return False

    def add_equipment(self, equip: Equipment):
        if equip not in self.equipment:
            self.equipment.append(equip)
        return False

    def add_plan(self, pl: ExercisePlan):
        if pl not in self.plans:
            self.plans.append(pl)
        return False

    def add_subscription(self, subs: Subscription):
        if subs not in self.subscriptions:
            self.subscriptions.append(subs)
        return False

    def subscription_info(self, subscription_id: int):
        csub: Subscription = [subs for subs in self.subscriptions if subs.id == subscription_id][0]
        client: Customer = [cl for cl in self.customers if csub.customer_id == cl.id][0]
        train: Trainer = [coach for coach in self.trainers if csub.trainer_id == coach.id][0]
        ex_plan: ExercisePlan = [plan for plan in self.plans if plan.id == csub.trainer_id][0]
        equip: Equipment = [quip for quip in self.equipment if quip.id == ex_plan.equipment_id][0]
        result = ""
        result += f'{csub}\n{client}\n{train}\n{equip}\n{ex_plan}'
        return result



