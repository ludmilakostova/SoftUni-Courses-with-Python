def is_index_valid(collection: list, index: int):
    if 0 <= index < len(collection):
        return True
    else:
        return False


def is_target_shoot(collection: list, target_index: int, power: int):
    if is_index_valid(collection, target_index):
        collection[target_index] -= power

        if collection[target_index] <= 0:
            collection.pop(target_index)

    return collection


def add_target(collection: list, index_target: int, value: int):
    if is_index_valid(collection, index_target):
        collection.insert(index_target, value)
    else:
        print(f'Invalid placement!')

    return collection


def is_strike(collection: list, index_t: int, radius: int):
    left_strike_index = index_t - radius
    right_strike_index = index_t + radius

    if is_index_valid(collection, index_t) and is_index_valid(collection, left_strike_index) and is_index_valid(collection, right_strike_index):
        for i in range(left_strike_index, right_strike_index+1):
            collection.pop(left_strike_index)
    else:
        print(f'Strike missed!')

    return collection


sequence = [int(el) for el in input().split()]
command = input()
while command != "End":
    command_as_list = command.split()
    command_args = command_as_list[0]
    command_index = int(command_as_list[1])
    command_value = int(command_as_list[2])

    if command_args == "Shoot":
        sequence = is_target_shoot(sequence, command_index, command_value)
    elif command_args == "Add":
        sequence = add_target(sequence, command_index, command_value)
    elif command_args == "Strike":
        sequence = is_strike(sequence, command_index, command_value)

    command = input()

sequence_as_string = [str(el) for el in sequence]
print('|'.join(sequence_as_string))
