numbers_dictionary = {}


while True:
    key = input()
    if key == "Search":
        break
    value = input()
    if value == "Search":
        break
    try:
        number = int(value)
        numbers_dictionary[key] = number
    except ValueError:
        print(f'The variable number must be an integer')
        break

line = input()

while line != "Remove":
    searched = line
    print(numbers_dictionary.get(searched, 'Number does not exist in dictionary'))
    line = input()


line = input()

while line != "End":
    searched = line
    try:
        del numbers_dictionary[searched]
        line = input()
    except KeyError:
        print(f'Number does not exist in dictionary')
        break

print(numbers_dictionary)
