string_one, string_two = input().split()
sum_characters = 0
if len(string_one) == len(string_two):
    for index in range(len(string_one)):
        sum_characters += ord(string_one[index]) * ord(string_two[index])
else:
    if len(string_one) > len(string_two):
        for index in range(len(string_two)):
            sum_characters += ord(string_one[index]) * ord(string_two[index])
        for index in range(len(string_two), len(string_one)):
            sum_characters += ord(string_one[index])
    else:
        for index in range(len(string_one)):
            sum_characters += ord(string_one[index]) * ord(string_two[index])
        for index in range(len(string_one), len(string_two)):
            sum_characters += ord(string_two[index])

print(sum_characters)


