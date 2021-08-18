number_heroes = int(input())
heroes_collection = {}
while not number_heroes == 0:
    heroes_name, hit_points, mana_points = input().split(" ")
    hit_points = int(hit_points)
    mana_points = int(mana_points)
    if heroes_name not in heroes_collection:
        heroes_collection[heroes_name] = {"hit points": hit_points, "mana points": mana_points}
    number_heroes -= 1

command = input()
while not command == "End":
    instruction = command.split(" - ")
    key_word = instruction[0]
    heroes_name = instruction[1]
    if key_word == "CastSpell":
        mana_points_needed = int(instruction[2])
        spell_name = instruction[3]
        if mana_points_needed <= heroes_collection[heroes_name]["mana points"]:
            heroes_collection[heroes_name]['mana points'] -= mana_points_needed
            print(
                f"{heroes_name} has successfully cast {spell_name} and now has {heroes_collection[heroes_name]['mana points']} MP!")
        else:
            print(f"{heroes_name} does not have enough MP to cast {spell_name}!")
    elif key_word == "TakeDamage":
        damage = int(instruction[2])
        attacker = instruction[3]
        heroes_collection[heroes_name]['hit points'] -= damage
        if heroes_collection[heroes_name]['hit points'] > 0:
            print(
                f"{heroes_name} was hit for {damage} HP by {attacker} and now has {heroes_collection[heroes_name]['hit points']} HP left!")
        else:
            del heroes_collection[heroes_name]
            print(f'{heroes_name} has been killed by {attacker}!')
    elif key_word == "Recharge":
        amount = int(instruction[2])
        old_mana_points = heroes_collection[heroes_name]['mana points']
        heroes_collection[heroes_name]['mana points'] += amount
        if heroes_collection[heroes_name]['mana points'] > 200:
            heroes_collection[heroes_name]['mana points'] = 200
        amount_recovered = heroes_collection[heroes_name]['mana points'] - old_mana_points
        print(f'{heroes_name} recharged for {amount_recovered} MP!')

    elif key_word == "Heal":
        amount = int(instruction[2])
        old_hit_points = heroes_collection[heroes_name]['hit points']
        heroes_collection[heroes_name]['hit points'] += amount
        if heroes_collection[heroes_name]['hit points'] > 100:
            heroes_collection[heroes_name]['hit points'] = 100
        amount_recovered = heroes_collection[heroes_name]['hit points'] - old_hit_points
        print(f"{heroes_name} healed for {amount_recovered} HP!")

    command = input()

sorted_collection = sorted(heroes_collection.items(), key=lambda tkvp: (-tkvp[1]['hit points'], tkvp[0]))
for hero, data in sorted_collection:
    print(f'{hero}\n  HP: {data["hit points"]}\n  MP: {data["mana points"]}')
