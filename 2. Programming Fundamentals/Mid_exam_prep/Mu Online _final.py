dungeons_room = input().split('|')
health = 100
bitcoins = 0
rooms_count = 0
for el in dungeons_room:
    el_string = ''.join(el)
    command, number = el_string.split(" ")
    number = int(number)
    rooms_count += 1
    if command == "potion":
        health += number
        if health <= 100:
            print(f"You healed for {number} hp.")
        else:
            print(f"You healed for {100 - (health - number)} hp.")
        if health > 100:
            health = 100
        print(f'Current health: {health} hp.')
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.\nBest room: {rooms_count}')
            break
if health > 0:
    print(f'You\'ve made it!')
    print(f'Bitcoins: {bitcoins}')
    print(f'Health: {health}')


