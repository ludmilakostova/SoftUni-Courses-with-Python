import sys
students_count = int(input())
lectures_count = int(input())
initial_bonus = int(input())
total_bonus = 0
max_total_bonus = -sys.maxsize
attendance_student = 0
while students_count > 0:
    attendance_per_student = int(input())
    total_bonus = attendance_per_student / lectures_count * (5 + initial_bonus)
    if total_bonus >= max_total_bonus:
        max_total_bonus = round(total_bonus)
        attendance_student = attendance_per_student
    students_count -= 1

result = f"Max Bonus: {max_total_bonus}.\nThe student has attended {attendance_student} lectures."
print(result)
