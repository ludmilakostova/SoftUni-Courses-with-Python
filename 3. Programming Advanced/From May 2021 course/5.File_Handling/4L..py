import os

try:
    os.remove("../File/my_first_file.txt")
except FileNotFoundError:
    print("File already deleted!")

