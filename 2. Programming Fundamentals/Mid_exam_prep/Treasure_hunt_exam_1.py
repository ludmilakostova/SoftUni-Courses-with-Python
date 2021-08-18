initial_loot = input().split('|')
command = input()
stolen_items = ''
stolen_items_list = []
while not command == "Yohoho!":
    command_data = command.split()
    command_order = command_data[0]
    if command_order == "Loot":
        for index in range(1, len(command_data)):
            if command_data[index] not in initial_loot:
                initial_loot.insert(0, command_data[index])
    elif command_order == "Drop":
        index = int(command_data[1])
        if 0 <= index < len(initial_loot):
            item = initial_loot[index]
            if item in initial_loot:
                initial_loot.remove(item)
                initial_loot.append(item)
    elif command_order == "Steal":
        count = int(command_data[1])
        start_range = len(initial_loot) - 1
        end_range = len(initial_loot) - count - 1
        if end_range < -1:
            end_range = -1
        for i in range(start_range, end_range, -1):
            stolen_items = initial_loot.pop(i)
            stolen_items_list.append(stolen_items)
        result = stolen_items_list[::-1]
        print(', '.join(result))
    command = input()

length_item = 0
for el in initial_loot:
    length_item += len(el)

if len(initial_loot) > 0:
    average_gain = length_item / len(initial_loot)
    print(f'Average treasure gain: {average_gain:.2f} pirate credits.')
else:
    print(f'Failed treasure hunt.')
