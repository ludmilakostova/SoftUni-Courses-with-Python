initial_array = [int(num) for num in input().split()]
command = input()
while not command == "end":
    command_list = command.split()
    key_word = command_list[0]
    if key_word == "swap":
        index_one = int(command_list[1])
        index_two = int(command_list[2])
        initial_array[index_one], initial_array[index_two] = initial_array[index_two], initial_array[index_one]
    elif key_word == "multiply":
        index_one = int(command_list[1])
        index_two = int(command_list[2])
        new_element = initial_array[index_one]*initial_array[index_two]
        initial_array[index_one] = new_element
    elif key_word == "decrease":
        for i in range(len(initial_array)):
            initial_array[i] -= 1

    command = input()

initial_array_str = [str(num) for num in initial_array]
print(', '.join(initial_array_str))

