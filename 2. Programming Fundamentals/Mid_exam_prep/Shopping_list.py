initial_list = input().split('!')
command = input()
while not command == "Go Shopping!":
    command_list = command.split()
    order = command_list[0]
    item = command_list[1]
    if order == "Urgent":
        if item not in initial_list:
            initial_list.insert(0, item)
    elif order == "Unnecessary":
        for el in initial_list:
            if item == el:
                initial_list.remove(el)

    elif order == "Correct":
        new_item = command_list[2]
        for index in range(len(initial_list)):
            if initial_list[index] == item:
                initial_list.insert(index+1, new_item)
                initial_list.pop(index)
    elif order == "Rearrange":
        for index in range(len(initial_list)):
            if item == initial_list[index]:
                removed_item = initial_list.pop(index)
                initial_list.append(removed_item)
    command = input()

print(', '.join(initial_list))


