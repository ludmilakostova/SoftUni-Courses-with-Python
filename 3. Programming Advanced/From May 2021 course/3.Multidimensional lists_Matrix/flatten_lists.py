command = input().split("|")
result = []
for i in range(len(command)-1, -1, -1):
    sublist = command[i].split()
    for el in sublist:
        result.append(el)
print(" ".join(result))