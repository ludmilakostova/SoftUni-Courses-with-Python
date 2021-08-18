def is_potion(num:int):
    health = 100
    health += number
    if health <= 100:
        print(f"You healed for {number} hp.")
    else:
        print(f"You healed for {100 - (health - number)} hp.")
    if health > 100:
        health = 100
        print(f'Current health: {health} hp.')

def is_chest(num:int):
    bitcoins += number
    print(f"You found {number} bitcoins.")

def all_other_cases(num:int):
    health -= number
    if health > 0:
        print(f'You slayed {command}.')
    else:
        print(f'You died! Killed by {command}.\nBest room: {rooms_count}')


dungeons_room = input().split('|')
health = 100
bitcoins = 0
rooms_count = 0
result = ''
for el in dungeons_room:
    el_string = ''.join(el)
    command, number = el_string.split(" ")
    number = int(number)
    rooms_count += 1
    if command == "potion":
        result = is_potion(number)
    elif command == "chest":
        result = is_chest(number)
    else:
        result = all_other_cases(number)
        break

if health > 0:
    print(f'You\'ve made it!')
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')

