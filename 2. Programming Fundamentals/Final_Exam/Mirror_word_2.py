import re

text = input()

pattern = r"(?P<surr>@|#)(?P<Word1>[A-Za-z]{3,})(?P=surr){2}(?P<Word2>[A-Za-z]{3,})(?P=surr)"
mirror_words = []
word_pairs = re.finditer(pattern, text)

count = 0
for word_pair in word_pairs:
    count += 1
    word_1 = word_pair.group('Word1')
    word_2 = word_pair.group('Word2')
    reversed_word_2 = word_2[::-1]

    if word_1 == reversed_word_2:
        mirror_words.append(f'{word_1} <=> {word_2}')

if count == 0:
    print(f'No word pairs found!')
else:
    print(f"{count} word pairs found!")

if not mirror_words:
    print(f"No mirror words!")
else:
    print(f'The mirror words are:')
    print(", ".join(mirror_words))