from math_operations.fibonnacci.helper import generate_sequence, find_number

command = input()

while not command == "Stop":
    data = command.split()
    if data[0] == "Create":
        print(generate_sequence(int(data[-1])))
    else:
        result = find_number(int(data[-1]), generate_sequence(int(data[-1])))
        print(f'The number - {int(data[-1])} is at index {result}' if isinstance(result, int) else result)
    command = input()
