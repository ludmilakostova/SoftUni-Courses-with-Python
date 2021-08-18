neighborhood_string = input().split('@')
neighborhood_list_int = [int(el) for el in neighborhood_string]
command = input()
index = 0
while not command == "Love!":
    order, length = command.split()
    length = int(length)
    if index < len(neighborhood_list_int):
        index += length
    if index >= len(neighborhood_list_int):
        index = 0
    if neighborhood_list_int[index] == 0:
        print(f'Place {index} already had Valentine\'s day.')
    else:
        neighborhood_list_int[index] -= 2
        if neighborhood_list_int[index] == 0:
            print(f'Place {index} has Valentine\'s day.')
    command = input()

print(f'Cupid\'s last position was {index}.')
count_houses = 0
if sum(neighborhood_list_int) == 0:
    print(f'Mission was successful.')
else:
    for el in neighborhood_list_int:
        if el > 0:
            count_houses += 1
    print(f'Cupid has failed {count_houses} places.')
