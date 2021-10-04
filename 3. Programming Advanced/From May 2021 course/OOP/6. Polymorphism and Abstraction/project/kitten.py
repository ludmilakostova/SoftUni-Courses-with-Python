from project.cat import Cat


class Kitten(Cat):
    gender = "Female"

    def __init__(self, name, age):
        super().__init__(name, age, __class__.gender)

    def make_sound(self):
        return 'Meow'

k= Kitten("Mila", 38)
print(k.gender)


