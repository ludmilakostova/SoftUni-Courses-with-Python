from Project_Lab_two.animal import Animal


class Dog(Animal):
    def bark(self):
        return "barking..."


d = Dog()
print(d.eat())
print(d.bark())
