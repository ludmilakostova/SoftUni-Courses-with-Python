command = input()
total = 0
while command != 'NoMoreMoney':
    installment = float(command)
    if installment >= 0:
        print(f'Increase: {installment:.2f}')
        total += installment
        command = input()
        continue
    if installment < 0:
        print(f'Invalid operation!')
        break

print(f'Total: {total:.2f}')

