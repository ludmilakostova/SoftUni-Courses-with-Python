number_of_rooms = int(input())
chairs_per_room = 0
total_visitors = 0
total_chairs = 0
for i in range(1, number_of_rooms + 1):
    command = input().split()
    count_chair = command[0]
    count_chair_list = list(count_chair)
    total_chairs += count_chair_list.count('X')
    chairs_per_room = len(count_chair_list)
    visitors_number = int(command[1])
    total_visitors += visitors_number
    if visitors_number > chairs_per_room:
        needed_chairs = visitors_number - chairs_per_room
        print(f'{needed_chairs} more chairs needed in room {i}')
if total_visitors <= total_chairs:
    print(f'Game On, {total_chairs - total_visitors} free chairs left')
