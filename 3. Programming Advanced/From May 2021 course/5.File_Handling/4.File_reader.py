file = open("../File/numbers.txt")
print(sum([int(el[:-1]) for el in file.readlines()]))