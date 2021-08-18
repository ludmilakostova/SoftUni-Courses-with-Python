number_commands = int(input())
registered_dict = {}
while number_commands > 0:
    command_list = input().split()
    key_word = command_list[0]
    user_name = command_list[1]
    if key_word == "register":
        plate = command_list[2]
        if user_name not in registered_dict:
            registered_dict[user_name] = plate
            print(f'{user_name} registered {registered_dict[user_name]} successfully')
        else:
            print(f'ERROR: already registered with plate number {registered_dict[user_name]}')
    elif key_word == "unregister":
        if user_name not in registered_dict:
            print(f'ERROR: user {user_name} not found')
        else:
            print(f'{user_name} unregistered successfully')
            registered_dict.pop(user_name)
    number_commands -= 1

for user_name, plate in registered_dict.items():
    print(f'{user_name} => {plate}')
