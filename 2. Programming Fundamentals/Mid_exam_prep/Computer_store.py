command = input()
total_price = 0
taxes = 0
while (not command == 'special') and (not command == 'regular'):
    price = float(command)
    if price >= 0:
        total_price += price
    else:
        print(f'Invalid price!')
    command = input()

if total_price == 0:
    print(f'Invalid order!')
else:
    taxes = 0.20 * total_price
    total_price_taxes = total_price + taxes
    if command == 'special':
        total_price_taxes = total_price_taxes * 0.9
    print(f'Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_price:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print(f'-----------')
    print(f'Total price: {total_price_taxes:.2f}$')


