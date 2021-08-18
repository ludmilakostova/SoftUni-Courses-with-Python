sequence_initial = input().split(", ")
result = ""
sequence_final = ""
for word in sequence_initial:
    if 3 <= len(word) <= 16:
        for character in word:
            if character.isalpha() or character.isdigit() or character == "-" or  character == "_":
                result += character
            else:
                break
        if len(word) == len(result):
            sequence_final += result + ", "
        result = ""

sequence_final_list = sequence_final.split(", ")
for word in sequence_final_list:
    if len(word) > 1:
        print(word)