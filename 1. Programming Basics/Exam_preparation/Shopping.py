budget = float(input())
video_number = int(input())
processor_number = int(input())
ram_number = int(input())
expenses = video_number * 250 + (0.35 * (250 * video_number) * processor_number) + 0.1 * (250 * video_number) * ram_number
if video_number > processor_number:
    expenses = 0.85 * expenses
profit_loss = budget - expenses
if budget >= expenses:
    print(f'You have {profit_loss:.2f} leva left!')
else:
    print(f'Not enough money! You need {abs(profit_loss):.2f} leva more!')


