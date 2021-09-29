from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        self.guests -= room.guests
        room.free_room()

    def status(self):
        number_free_rooms = [r.number for r in self.rooms if not r.is_taken]
        number_taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return f'Hotel {self.name} has {self.guests} total guests\n' \
               f'Free rooms: {", ".join(map(str, number_free_rooms))}\n' \
               f'Taken rooms: {", ".join(map(str, number_taken_rooms))}'



hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())
