pastry_name = input()
pastry_number = int(input())
day = int(input())
pastry_expenses = 0
if day <= 15:
    if pastry_name == 'Cake':
        pastry_expenses = 24 * pastry_number
    elif pastry_name == 'Souffle':
        pastry_expenses = 6.66 * pastry_number
    elif pastry_name == 'Baklava':
        pastry_expenses = 12.60 * pastry_number
else:
    if pastry_name == 'Cake':
        pastry_expenses = 28.70 * pastry_number
    elif pastry_name == 'Souffle':
        pastry_expenses = 9.80 * pastry_number
    elif pastry_name == 'Baklava':
        pastry_expenses = 16.98 * pastry_number
if day <= 22:
    if 100 <= pastry_expenses < 200:
        pastry_expenses = 0.85 * pastry_expenses
    elif pastry_expenses >= 200:
        pastry_expenses = 0.75 * pastry_expenses
    if day <= 15:
        pastry_expenses = 0.90 * pastry_expenses
print(f'{pastry_expenses:.2f}')

