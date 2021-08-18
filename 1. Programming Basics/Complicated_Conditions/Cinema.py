type_screening = input()
rows_number = int(input())
columns_number = int(input())
price = 0
if type_screening == "Premiere":
    price = 12
elif type_screening == "Normal":
    price = 7.50
elif type_screening == "Discount":
    price = 5.00
income = price * rows_number * columns_number
print(f'{income:.2f} leva')