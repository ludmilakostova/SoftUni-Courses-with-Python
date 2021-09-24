seq_one = set([int(el) for el in input().split()])
seq_two = set([int(el) for el in input().split()])
number_commands = int(input())

while number_commands > 0:
    key, part, *res = input().split()
    res = [int(el) for el in res]
    if key == "Add":
        if part == "First":
            for el in res:
                seq_one.add(el)
        elif part == "Second":
            for el in res:
                seq_two.add(el)

    elif key == "Remove":
        if part == "First":
            for el in res:
                if el in seq_one:
                    seq_one.remove(el)
        elif part == "Second":
            for el in res:
                if el in seq_two:
                    seq_two.remove(el)

    elif key == "Check":
        print(seq_one.issubset(seq_two) or seq_two.issubset(seq_one))

    number_commands -= 1

print(", ".join(str(el) for el in sorted(seq_one)))
print(", ".join(str(el) for el in sorted(seq_two)))
