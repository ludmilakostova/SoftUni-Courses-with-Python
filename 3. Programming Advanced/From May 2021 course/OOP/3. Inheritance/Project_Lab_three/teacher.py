from Project_Lab_three.employee import Employee
from Project_Lab_three.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


t = Teacher()
print(t.sleep())
print(t.get_fired())
print(t.teach())