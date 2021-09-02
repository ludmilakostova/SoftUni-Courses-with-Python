import re
with open("../File/words.txt") as file:
    searched_words = file.read().split()

occs = {}
with open("../File/text.txt") as file:
    content = file.read().lower()
    for word in searched_words:
        result = re.findall(rf"(?<=(\-|\s)){word}(?=(\.|\s))", content)
        occs[word] = len(result)

sorted_result = sorted(occs.items(), key= lambda x: -x[1])
for key, value in sorted_result:
    print(f"{key} - {value}")