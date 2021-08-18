command = [int(el) for el in input().split(', ')]
positive_list = [el for el in command if el >= 0]
negative_list = [el for el in command if el < 0]
even_list = [el for el in command if el % 2 == 0]
odd_list = [el for el in command if el % 2 == 1]
positive_list_as_string = [str(el) for el in positive_list]
negative_list_as_string = [str(el) for el in negative_list]
even_list_as_string = [str(el) for el in even_list]
odd_list_as_string = [str(el) for el in odd_list]
print(f'Positive: {", ".join(positive_list_as_string)}')
print(f'Negative: {", ".join(negative_list_as_string)}')
print(f'Even: {", ".join(even_list_as_string)}')
print(f'Odd: {", ".join(odd_list_as_string)}')
