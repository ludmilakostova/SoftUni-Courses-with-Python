def sum_numbers(num_1, num_2):
    result = num_1 + num_2
    return result


def subtract(sum_1, number_3):
    result = sum_1 - number_3
    return result


def add_and_subtract(n1, n2, n3):
    sum_1 = sum_numbers(n1, n2)
    result = subtract(sum_1, n3)
    return result


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
result_subtract = add_and_subtract(num_1, num_2, num_3)
print(result_subtract)
