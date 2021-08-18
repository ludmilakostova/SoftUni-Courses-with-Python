import re

text = input()
pattern = r"\s[A-Za-z0-9]+([\.\-_])?[a-z0-9]+@[a-z]+(\-)?[a-z]+(\.)[a-z]+(\.[a-z]+)?\b"
valid_emails = re.finditer(pattern, text)
for email in valid_emails:
    print(email.group())

