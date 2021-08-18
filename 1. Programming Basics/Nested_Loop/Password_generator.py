Xn = int(input())
Xl = int(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
for a in range(1, Xn):
    for b in range(1, Xn):
        for c_index in range(Xl):
            c = alphabet[c_index]
            for d_index in range(Xl):
                d = alphabet[d_index]
                for e in range(1, Xn + 1):
                    if e > a and e > b:
                        print(f'{a}{b}{c}{d}{e}', end=" ")
