def palindrome(command: str):
    is_palindrome = False
    for element in command:
        element = str(element)
        for index in range(len(element)):
            if element[index] == element[-index - 1]:
                is_palindrome = True
            else:
                break
        return is_palindrome


command_input = input().split(', ')
for i in range(len(command_input)):
    command_input[i] = int(command_input[i])
for i in range(len(command_input)):
    print(palindrome(command_input))
    command_input.remove(command_input[0])
