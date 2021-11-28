class DecorationRepository:
    def __init__(self):
        self.decorations = []

    def add(self, decoration):
        self.decorations.append(decoration)

    def remove(self, decoration):
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        try:
            type_deco = [d for d in self.decorations if decoration_type == d.__class__.__name__][0]
            return type_deco
        except IndexError:
            return 'None'

