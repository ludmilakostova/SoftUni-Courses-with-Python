import math
people = int(input())
entry_fee = float(input())
bed_fee = float(input())
umbrella_fee = float(input())
total_entry_fee = people * entry_fee
total_bed_fee = math.ceil(0.75 * people) * bed_fee
total_umbrella_fee = math.ceil(people / 2) * umbrella_fee
total_expenses = total_bed_fee + total_umbrella_fee + total_entry_fee
print(f'{total_expenses:.2f} lv.')
