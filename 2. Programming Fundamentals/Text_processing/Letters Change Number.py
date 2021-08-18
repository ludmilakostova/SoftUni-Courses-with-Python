import string
initial_sequence = input().split()
i = 0
number = ""
number_first_letter = 0
result = 0
final_result = 0
while i < len(initial_sequence):
    first_letter = initial_sequence[i][:1]
    for y in range(1, len(initial_sequence[i]) - 1):
        if initial_sequence[i][y:y + 1].isdigit():
            number += initial_sequence[i][y:y + 1]
        else:
            break

    number = int(number)
    firs_letter_case_insensitive = first_letter.lower()
    first_letter_position = string.ascii_lowercase.index(firs_letter_case_insensitive) + 1

    if first_letter.isupper():
        number_first_letter = number / first_letter_position
    else:
        number_first_letter = number * first_letter_position

    last_letter = initial_sequence[i][-1]
    last_letter_case_insensitive = last_letter.lower()
    last_letter_position = string.ascii_lowercase.index(last_letter_case_insensitive) + 1
    if last_letter.isupper():
        result = number_first_letter - last_letter_position
    else:
        result = number_first_letter + last_letter_position

    final_result += result
    i += 1
    number = str('')

print(f"{final_result:.2f}")
