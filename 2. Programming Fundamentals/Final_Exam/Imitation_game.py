encrypted_message = input()

command = input()

to_move = ""
while not command == "Decode":
    instruction = command.split("|")
    key_word = instruction[0]
    if key_word == "Move":
        number_letters = int(instruction[1])
        for i in range(number_letters):
            to_move += encrypted_message[i]
        new_encrypted_message = encrypted_message[number_letters:]+to_move
        encrypted_message = new_encrypted_message
        to_move = ''
    elif key_word == "Insert":
        index = int(instruction[1])
        value = instruction[2]
        new_encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
        encrypted_message = new_encrypted_message
    elif key_word == "ChangeAll":
        substring = instruction[1]
        replacement = instruction[2]
        encrypted_message = encrypted_message.replace(substring, replacement)

    command = input()

print(f'The decrypted message is: {encrypted_message}')