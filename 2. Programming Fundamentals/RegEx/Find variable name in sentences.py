import re

text = input()

pattern = r"(?<=\b_)[a-zA-Z0-9]+\b"
valid_names = re.finditer(pattern, text)
valid_names = [name.group() for name in valid_names]
print(",".join(valid_names))
