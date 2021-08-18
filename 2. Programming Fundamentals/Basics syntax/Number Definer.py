num = float(input())
if num == 0:
    print(f'zero')
elif num > 1000000:
    print(f'large positive')
elif num > 0:
    if num < 1:
        print(f' small positive')
    else:
        print(f'positive')
elif num < -1000000:
    print(f'large negative')
elif num < 0:
    if num > -1:
        print(f'small negative')
    else:
        print(f'negative')