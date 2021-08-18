import re
text = input().lower()
searched_word = input().lower()

pattern = rf"\b{searched_word}\b"
count = len(re.findall(pattern, text))
print(count)
