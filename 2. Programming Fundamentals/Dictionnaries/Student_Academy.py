pair_rows = int(input())
total_rows = 2 * pair_rows
students_dict = {}
for _ in range(0, total_rows, 2):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_dict:
        students_dict[student_name] = []
    students_dict[student_name].append(student_grade)

for student_name in students_dict:
    students_dict[student_name] = sum(students_dict[student_name]) / len(students_dict[student_name])

passed_student_dict = {student_name: student_grade for student_name, student_grade in students_dict.items() if
                       student_grade >= 4.50}

passed_student_dict_sorted = dict(sorted(passed_student_dict.items(), key=lambda x: -x[1]))
for student_name, student_grade in passed_student_dict_sorted.items():
    print(f'{student_name} -> {student_grade:.2f}')
