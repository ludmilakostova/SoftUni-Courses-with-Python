def list_manipulator(sequence: [], key_instruction: str, location: str, *args):
    if key_instruction == "add":
        args = list(args)
        if location == "beginning":
            sequence = args + sequence
        elif location == "end":
            sequence += args
    elif key_instruction == "remove":
        if location == "beginning":
            if len(args) > 0:
                count_to_remove = int(args[0])
                for rotation in range(count_to_remove):
                    sequence.remove(sequence[0])
            else:
                sequence.remove(sequence[0])
        elif location == "end":
            if len(args) > 0:
                count_to_remove = int(args[0])
                for rotation in range(count_to_remove):
                    sequence.pop()
            else:
                sequence.pop()
    return sequence



print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
