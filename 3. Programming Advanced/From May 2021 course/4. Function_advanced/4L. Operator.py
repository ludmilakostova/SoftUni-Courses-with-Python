# from functools import reduce
#
#
# def operate(operator: str, *args: int):
#     if operator == "+":
#         return reduce(lambda x, y: x + y, args)
#     elif operator == "-":
#         return reduce(lambda x, y: x - y, args)
#     elif operator == "*":
#         return reduce(lambda x, y: x * y, args)
#     elif operator == "/":
#         return reduce(lambda x, y: x / y, args)
#
#
# print(operate("*", 3, 4))

# Option 2 with eval
from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f'{x}{operator}{y}'), args)


print(operate("*", 3, 4))
