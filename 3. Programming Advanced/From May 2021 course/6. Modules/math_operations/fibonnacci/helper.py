def generate_sequence(n):
    seq = [0, 1]

    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def find_number(num, seq):
    if num in seq:
        return seq.index(num)
    return "The n"



