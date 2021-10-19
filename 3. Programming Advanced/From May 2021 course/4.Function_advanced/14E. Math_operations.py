def math_operations(*args, **kwargs):
    sequence = list(args)
    for i in range(0, len(sequence), 4):
        if len(sequence[i:]) >= 1:
            kwargs['a'] += sequence[i]
        else:
            break
        if len(sequence[i + 1:]) >= 1:
            kwargs['s'] -= sequence[i + 1]
        else:
            break
        if len(sequence[i + 2:]) >= 1 and sequence[i + 2] != 0:
            kwargs['d'] /= sequence[i + 2]
        if len(sequence[i + 3:]) >= 1:
            kwargs['m'] *= sequence[i + 3]
        else:
            break

    return kwargs


print(math_operations(6, a=0, s=0, d=0, m=0))
