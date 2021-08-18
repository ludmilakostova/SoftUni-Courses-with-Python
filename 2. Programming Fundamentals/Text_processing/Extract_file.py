initial_sequence = input().split("\\")
key_word = initial_sequence[-1]
key_position = key_word.find(".")
format_file = key_word[key_position+1:]
file_name = key_word[:key_position]
print(f'File name: {file_name}')
print(f'File extension: {format_file}')
