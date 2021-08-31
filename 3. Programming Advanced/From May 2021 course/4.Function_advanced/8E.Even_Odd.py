def even_odd(*args):
    command = args[-1]
    new_sequence = args[:-1]
    if command == "even":
        result = list(filter(lambda x: x % 2 == 0, new_sequence))
    elif command == "odd":
        result = list(filter(lambda x: x % 2 == 1, new_sequence))
    return result


even_odd(1, 2, 3, 4, 5, 6, "even")
