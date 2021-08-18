sequence = input()
new_char = ""
for char in sequence:
    new_char_number = ord(char) + 3
    new_char += chr(new_char_number)

print(new_char)