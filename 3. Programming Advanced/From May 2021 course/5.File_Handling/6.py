import os

try:
    os.remove("../File/example.txt")
except FileNotFoundError:
    print("File does not exist")
