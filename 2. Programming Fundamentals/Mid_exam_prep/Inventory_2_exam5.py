collecting_items = input().split(", ")
command, item = input().split(" - ")
while not command == "Craft!":

    if command == "Collect":
        if item not in collecting_items:
            collecting_items.append(item)

    elif command == "Drop":
        collecting_items = [collecting_items.remove(el) for el in collecting_items if el == item]

    elif command == "Combine Items":
        item_str = ''.join(item)
        old_item, new_item = item_str.split(':')
        for index in range(len(collecting_items)):
            if collecting_items[index] == old_item:
                collecting_items.insert((index+1), new_item)

    elif command == "Renew":
        for index in range(len(collecting_items)):
            if collecting_items[index] == item:
                collecting_items.append(item)
                collecting_items.remove(item)
                break
    new_command = input()
    if new_command == 'Craft!':
        command = new_command
    else:
        command, item = new_command.split(" - ")

print(", ".join(collecting_items))
