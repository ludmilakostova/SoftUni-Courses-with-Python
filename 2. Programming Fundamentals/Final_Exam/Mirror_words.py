import re

text = input()
word_list = []
pattern = r"(?P<surr>@|#)(?P<Word1>[A-Za-z]{3,})(?P=surr){2}(?P<Word2>[A-Za-z]{3,})(?P=surr)"
word_pairs = re.finditer(pattern, text)
for word_pair in word_pairs:
    current_word_pair = word_pair.groupdict()
    word_list.append(current_word_pair['Word1'])
    word_list.append(current_word_pair['Word2'])

if not word_list:
    print(f'No word pairs found!')
else:
    print(f"{(len(word_list))//2} word pairs found!")

mirror_words = []
for i in range(0, len(word_list), 2):
    reversed_word = word_list[i+1][::-1]
    if word_list[i] == reversed_word:
        mirror_words.append(word_list[i])
        mirror_words.append(word_list[i+1])
if not mirror_words:
    print(f"No mirror words!")
else:
    print(f'The mirror words are:')
    for i in range(0, len(mirror_words), 2):
        print(f'{mirror_words[i]} <=> {mirror_words[i+1]}', end=", ")
