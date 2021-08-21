stack = []
number_queries = int(input())

while number_queries > 0:
    command = input()
    if command.startswith("1"):
        number = command.split()[-1]
        stack.append(int(number))
    elif command.startswith("2"):
        if len(stack) > 0:
            stack.pop()
    elif command.startswith("3"):
        if len(stack) > 0:
            print(f'{max(stack)}')
    elif command.startswith("4"):
        if len(stack) > 0:
            print(f'{min(stack)}')

    number_queries -= 1
reversed_stack = []
for i in range(len(stack)):
    reversed_stack.append(str(stack.pop()))
print(", ".join(reversed_stack))
