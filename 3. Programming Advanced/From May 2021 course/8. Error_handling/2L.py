class ValueCannotBeNegative(Exception):
    """"Raised when the input value is negative"""
    pass


for i in range(5):
    number = float(input())
    if number < 0:
        raise ValueCannotBeNegative
