initial_list = input().split(" | ")
dictionary = {}
for element in initial_list:
    word, definition = element.split(": ")
    if word not in dictionary:
        dictionary[word] = []
    dictionary[word].append(definition)

words_test = input().split(" | ")
command = input()
if command == "Test":
    for word_test in words_test:
        if word_test in dictionary:
            definition = dictionary[word_test]
            sorted_definition = list(sorted(definition, key=len, reverse=True))
            print(f'{word_test}:')
            for el in sorted_definition:
                print(f' -{el}')
elif command == "Hand Over":
    sorted_dictionary = sorted(dictionary.items(), key=lambda x: x[0])
    for key, value in sorted_dictionary:
        print(f'{key}', end=" ")
