names_of_gifts = input().split()
command = input().split()
while "No" not in command and "Money" not in command:
    if "OutOfStock" in command:
        lost_item = command[1]
        for i in range(len(names_of_gifts)):
            if names_of_gifts[i] == lost_item:
                names_of_gifts[i] = 'None'
    elif "Required" in command:
        command[2] = int(command[2])
        new_element = command[1]
        index = command[2]
        if index <= len(names_of_gifts) - 1:
            names_of_gifts[index] = new_element
    elif 'JustInCase' in command:
        names_of_gifts[-1] = command[1]
    command = input().split()

for i in range(len(names_of_gifts)):
    if "None" in names_of_gifts:
        names_of_gifts.remove("None")

print(' '.join(names_of_gifts))
