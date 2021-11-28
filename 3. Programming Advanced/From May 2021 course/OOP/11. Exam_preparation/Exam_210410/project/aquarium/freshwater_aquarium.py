from project.aquarium.base_aquarium import BaseAquarium


class FreshwaterAquarium(BaseAquarium):
    def __init__(self, name: str):
        super().__init__(name, 50)

    def add_fish(self, fish):
        if self.available_capacity <= 0:
            return f'Not enough capacity.'
        if fish.__class__.__name__ == "FreshwaterFish":
            self.fish.append(fish)
            return f'Successfully added {fish.__class__.__name__} to {self.name}.'
        return f'Water not suitable.'

