import re

collection = []
while True:
    text = input()
    if text:
        collection.append(text)
    else:
        break
list_string = (" ".join(collection))

pattern = r"\d+"
valid_numbers = re.findall(pattern, list_string)
print(*valid_numbers)

