age = int(input())
laundry_price = float(input())
toy_price = int(input())
toy_number = 0
saving = 0
for i in range(1, age + 1):
    if i % 2 == 0:
        saving = saving + i * 5 - 1
    else:
        toy_number += 1

toy_saving = toy_number * toy_price
total_saving = toy_saving + saving
remaining = total_saving - laundry_price

if remaining >= 0:
    print(f'Yes! {remaining:.2f}')
else:
    print(f'No! {abs(remaining):.2f}')

