def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*func_args: tuple, res=[]):
    for func, fargs in func_args:
        res.append(func(*fargs))
    return res


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
