initial_sequence = input()
emoticons = ""
i = 0
while i < len(initial_sequence):
    if initial_sequence[i] == ":":
        emoticons = initial_sequence[i] + initial_sequence[i + 1]
        print(emoticons)
        emoticons = ""

    i += 1
