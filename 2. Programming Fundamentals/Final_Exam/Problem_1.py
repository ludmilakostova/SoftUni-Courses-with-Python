username = input()
command = input()
while not command == "Sign up":
    instruction = command.split(" ")
    key_word = instruction[0]
    if key_word == "Case":
        type_case = instruction[1]
        if type_case == "lower":
            username = username.lower()
        elif type_case == "upper":
            username = username.upper()
        print(username)
    elif key_word == "Reverse":
        start_index = int(instruction[1])
        end_index = int(instruction[2])
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            substring = username[start_index:end_index + 1]
            new_substring = substring[::-1]
            print(new_substring)
    elif key_word == "Cut":
        substring = instruction[1]
        if substring in username:
            index_start = username.find(substring)
            length = len(substring)
            index_end = index_start + length
            new_username = username[:index_start] + username[index_end:]
            username = new_username
            print(username)
        else:
            print(f'The word {username} doesn\'t contain {substring}.')
    elif key_word == "Replace":
        char = instruction[1]
        username = username.replace(char, "*")
        print(username)
    elif key_word == "Check":
        char = instruction[1]
        if char in username:
            print("Valid")
        else:
            print(f'Your username must contain {char}.')

    command = input()
