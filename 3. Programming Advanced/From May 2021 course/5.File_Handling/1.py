from os import path

if path.exists("../File/text.txt"):
    print("File found")
else:
    print("File not found")

# Second way
try:
    open("../File/text.txt")
    print("File found")
except FileNotFoundError:
    print("File not found")
