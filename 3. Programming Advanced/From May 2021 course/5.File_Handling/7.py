import os
current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)
print(__file__)
path = os.path.join(current_directory, "..", "File", "text.txt")
print(path)

print(os.listdir("./"))