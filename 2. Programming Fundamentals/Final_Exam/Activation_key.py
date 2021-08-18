raw_activation_key = input()
command = input()

while not command == "Generate":
    command_list = command.split(">>>")
    key_word = command_list[0]
    if key_word == "Contains":
        substring = command_list[1]
        if substring in raw_activation_key:
            print(f'{raw_activation_key} contains {substring}')
        else:
            print(f'Substring not found!')

    elif key_word == "Flip":
        type_of_case = command_list[1]
        start_index = int(command_list[2])
        end_index = int(command_list[3])
        part_replacing = raw_activation_key[start_index:end_index]
        if type_of_case == "Upper":
            new_part = part_replacing.upper()
            raw_activation_key = raw_activation_key.replace(part_replacing, new_part)
        elif type_of_case == "Lower":
            new_part = part_replacing.lower()
            raw_activation_key = raw_activation_key.replace(part_replacing, new_part)
        print(raw_activation_key)
    elif key_word == "Slice":
        start_index = int(command_list[1])
        end_index = int(command_list[2])
        part = raw_activation_key[start_index:end_index]
        raw_activation_key = raw_activation_key.replace(part, "")
        print(raw_activation_key)

    command = input()

print(f'Your activation key is: {raw_activation_key}')