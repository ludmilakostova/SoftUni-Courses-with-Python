import os

command = input()
while not command == "End":
    key_word, *instruction = command.split("-")
    if key_word == "Create":
        with open(instruction[0], "w"):
            pass
    elif key_word == "Add":
        file_name, content = instruction
        with open(file_name, "a") as file:
            file.write(content + "\n")

    elif key_word == "Replace":
        file_name, old, new = instruction
        try:
            with open(file_name, "r") as file:
                content = file.read()

            with open(file_name, "w") as file:
                content = content.replace(old, new)
                file.write(content)
        except Exception as e:
            print("An error occurred")
            line = input()
            continue
    elif key_word == "Delete":
        try:
            os.remove(instruction[1])
        except FileNotFoundError:
            print("An error occurred")

    command = input()