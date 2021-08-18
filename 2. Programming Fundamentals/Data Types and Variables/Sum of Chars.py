n = int(input())
sum_symbol = 0
for i in range(1, n + 1):
    symbol = input()
    sum_symbol += ord(symbol)
print(f'The sum equals: {sum_symbol}')
