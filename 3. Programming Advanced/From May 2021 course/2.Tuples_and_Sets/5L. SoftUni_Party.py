number_guests = int(input())
guests_list = set()

for _ in range(number_guests):
    guests_list.add(input())

command = input()
while not command == "END":
    guests_list.discard(command)

    command = input()
sorted_list = sorted(guests_list)
print(len(sorted_list))
[print(el) for el in sorted_list]