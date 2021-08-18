import re

text = input()
cool_threshold = 1
full_emojis_collection = []

for i in range(len(text)):
    if text[i].isdigit():
        number = int(text[i])
        cool_threshold *= number
print(f"Cool threshold: {cool_threshold}")

pattern = r"(?P<Emojis>(?P<Start>:{2}|\*{2})(?P<Body>[A-Z][a-z]{2,})(?P=Start))"
emojis_detector = re.finditer(pattern, text)
for emoji in emojis_detector:
    current_emojis = emoji.groupdict()
    full_emojis_collection.append(current_emojis["Emojis"])
print(f'{len(full_emojis_collection)} emojis found in the text. The cool ones are:')

cool_level = 0

for emoji in full_emojis_collection:
    for i in range(len(emoji)):
        if emoji[i].isalpha():
            cool_level += ord(emoji[i])
    if cool_level >= cool_threshold:
        print(emoji)
    cool_level = 0
