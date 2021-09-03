with open("text.txt") as file:
    collection = ["-", ",", ".", "!", "?"]
    for index, line in enumerate(file.readlines()):
        if index % 2 != 0:
            continue
        result = ""
        for symbol in line.strip():
            if symbol in collection:
                symbol = "@"
            result += symbol
        result = result.split()
        result = result[::-1]
        print(" ".join(result))

# Option 2 with regex
# import re
# with open("text.txt") as file:
#     for idx, line in enumerate(file.readlines()):
#         if idx % 2 != 0:
#             continue
#         line = re.sub("[-.!?,]", "@", line)
#         line = " ".join(reversed(line.split()))
#         print(line.strip())








