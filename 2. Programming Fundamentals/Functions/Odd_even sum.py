def even_odd_sum_single_number(num_1: str):
    even_sum = 0
    odd_sum = 0
    for ch in num_1:
        digit = int(ch)
        if digit % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


single_number = input()
result = even_odd_sum_single_number(single_number)
print(result)
