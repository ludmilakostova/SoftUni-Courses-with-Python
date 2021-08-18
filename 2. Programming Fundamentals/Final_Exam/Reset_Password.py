password = input()
command = input()
new_password = ""
while not command == "Done":
    instruction = command.split(" ")
    key_word = instruction[0]
    if key_word == "TakeOdd":
        for i in range(len(password)):
            if i % 2 == 1:
                new_password += password[i]
        print(new_password)
        password = new_password
    elif key_word == "Cut":
        index = int(instruction[1])
        length = int(instruction[2])
        end_index = index + length
        substring = password[index:end_index]
        password = password.replace(substring, "", 1)
        print(password)
    elif key_word == "Substitute":
        substring_to_substitute = instruction[1]
        new_substring = instruction[2]
        if not substring_to_substitute in password:
            print(f"Nothing to replace!")
        else:
            while substring_to_substitute in password:
                password = password.replace(substring_to_substitute, new_substring)
            print(password)

    command = input()

print(f"Your password is: {password}")
