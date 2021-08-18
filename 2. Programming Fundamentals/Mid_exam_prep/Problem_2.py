initial_weapon_name = input().split("|")
command = input()
weapon_even = []
weapon_odd = []
while not command == "Done":
    command_list = command.split()
    key_word = command_list[0]
    if key_word == "Add":
        particle = command_list[1]
        index = int(command_list[2])
        if 0 <= index < len(initial_weapon_name):
            initial_weapon_name.insert(index, particle)
    elif key_word == "Remove":
        index = int(command_list[1])
        if 0 <= index < len(initial_weapon_name):
            initial_weapon_name.pop(index)
    elif key_word == "Check":
        part_two = command_list[1]
        if part_two == "Even":
            for i in range(len(initial_weapon_name)):
                if i % 2 == 0:
                    weapon_even.append(initial_weapon_name[i])
            print(" ".join(weapon_even))
        elif part_two == "Odd":
            for i in range(len(initial_weapon_name)):
                if i % 2 == 1:
                    weapon_odd.append(initial_weapon_name[i])
            print(" ".join(weapon_odd))
    command = input()

print(f'You crafted {"".join(initial_weapon_name)}!')
