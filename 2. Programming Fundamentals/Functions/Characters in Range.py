def characters_in_range(sym_1, sym_2):
    sym_1 = ord(sym_1)
    sym_2 = ord(sym_2)
    b = ''
    for i in range((sym_1 + 1), sym_2):
        b += chr(i)
    return b

symbol_1 = input()
symbol_2 = input()
result = characters_in_range(symbol_1, symbol_2)
for i in range(len(result)):
    print(f'{result[i]}', end=' ')