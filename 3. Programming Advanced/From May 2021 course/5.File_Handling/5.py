# With manager - the file will be automatically closed
with open("../File/numbers.txt") as file:
    result = 0
    for line in file:
        result += int(line)
    print(result)

