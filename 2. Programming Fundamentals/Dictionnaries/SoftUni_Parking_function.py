def register_unregister(final_register: dict, keyword: str, user: str):
    if keyword == "register":
        licence = command_list[2]
        if user not in final_register:
            final_register[user] = licence
            print(f'{user} registered {final_register[user]} successfully')
        else:
            print(f'ERROR: already registered with plate number {final_register[user]}')
    elif keyword == "unregister":
        if user not in final_register:
            print(f'ERROR: user {user} not found')
        else:
            print(f'{user} unregistered successfully')
            final_register.pop(user)


number_commands = int(input())
registered_dict = {}
while number_commands > 0:
    command_list = input().split()
    key_word = command_list[0]
    user_name = command_list[1]

    register_unregister(registered_dict, key_word, user_name)

    number_commands -= 1

for user_name, plate in registered_dict.items():
    print(f'{user_name} => {plate}')