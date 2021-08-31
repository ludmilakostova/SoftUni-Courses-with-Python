def possible_orders(expression, step=0):
    for i in range(step, len(expression)):
        new_string = [el for el in expression]
        new_string[step], new_string[i] = new_string[i], new_string[step]
        possible_orders(new_string, step+1)

    if step == len(expression):
        print("".join(expression))


expression = input()
possible_orders(expression)
