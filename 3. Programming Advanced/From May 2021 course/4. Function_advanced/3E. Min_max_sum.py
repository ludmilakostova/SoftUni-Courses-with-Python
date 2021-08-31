def min_max_sum(expression: list):
    min_el = min(expression)
    max_el = max(expression)
    sum_res = sum(expression)
    print(f'The minimum number is {min_el}')
    print(f'The maximum number is {max_el}')
    print(f'The sum number is: {sum_res}')


sequence = [int(el) for el in input().split()]
min_max_sum(sequence)
