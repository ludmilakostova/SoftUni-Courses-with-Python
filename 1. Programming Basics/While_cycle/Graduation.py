name = input()
class_num = 0
grades_sum = 0
bad_grades_count = 0
while bad_grades_count < 2:
    class_num += 1
    grade = float(input())
    grades_sum += grade
    if grade < 4:
        bad_grades_count += 1
        class_num -= 1

    if class_num == 12:
        break

if bad_grades_count != 2:
    print(f'{name} graduated. Average grade: {(grades_sum / class_num):.2f}')
else:
    print(f'{name} has been excluded at {class_num + 1} grade')