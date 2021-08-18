secret_message = input()
command = input()

while not command == "Reveal":
    instructions = command.split(":|:")
    key_word = instructions[0]
    if key_word == "InsertSpace":
        index = int(instructions[1])
        to_add = " "
        secret_message = secret_message[:index] + to_add + secret_message[index:]
        print(secret_message)
    elif key_word == "Reverse":
        substring = instructions[1]
        if substring in secret_message:
            reversed_substring = substring[::-1]
            secret_message = secret_message.replace(substring, "", 1)
            secret_message = secret_message + reversed_substring
            print(secret_message)
        else:
            print(f'error')
    elif key_word == "ChangeAll":
        substring = instructions[1]
        new_string = instructions[2]
        while substring in secret_message:
            secret_message = secret_message.replace(substring, new_string)
        print(secret_message)

    command = input()

print(f'You have a new text message: {secret_message}')