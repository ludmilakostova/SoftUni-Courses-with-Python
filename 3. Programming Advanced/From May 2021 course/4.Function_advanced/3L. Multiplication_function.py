# Option 1
# def multiply(*args):
#     result = 1
#     for el in args:
#         result *= el
#     return result
#
#
# print(multiply(1, 4, 5))

# Option 2
from functools import reduce


def multiply(*args):
    return reduce(lambda x, y: x * y, args)


print(multiply(1, 2, 4))
