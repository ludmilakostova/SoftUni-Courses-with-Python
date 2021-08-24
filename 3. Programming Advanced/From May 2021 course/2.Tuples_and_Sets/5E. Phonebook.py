phonebook = {}
while True:
    line = input()
    if line.isdigit():
        break
    name, number = line.split("-")
    phonebook[name] = number

for _ in range(int(line)):
    name = input()
    if name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')

