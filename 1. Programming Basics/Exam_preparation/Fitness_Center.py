visitors = int(input())
back_visitors = 0
chest_visitors = 0
legs_visitors = 0
Abs_visitors = 0
Protein_shake_visitors = 0
Protein_bar_visitors = 0
for i in range(1, visitors + 1):
    command = input()
    if command == "Back":
        back_visitors += 1
    elif command == "Chest":
        chest_visitors += 1
    elif command == "Legs":
        legs_visitors += 1
    elif command == "Abs":
        Abs_visitors += 1
    elif command == "Protein shake":
        Protein_shake_visitors += 1
    elif command == "Protein bar":
        Protein_bar_visitors += 1
training_visitors = (back_visitors + chest_visitors + legs_visitors + Abs_visitors)/ visitors * 100
feeding_visitors = (Protein_bar_visitors + Protein_shake_visitors)/ visitors * 100

print(f'{back_visitors} - back')
print(f'{chest_visitors} - chest')
print(f'{legs_visitors} - legs')
print(f'{Abs_visitors} - abs')
print(f'{Protein_shake_visitors} - protein shake')
print(f'{Protein_bar_visitors} - protein bar')
print(f'{training_visitors:.2f}% - work out')
print(f'{feeding_visitors:.2f}% - protein')


