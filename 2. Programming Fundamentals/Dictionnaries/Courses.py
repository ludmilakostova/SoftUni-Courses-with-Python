command = input()
registered_dict = {}
while not command == "end":
    course_name, registered_student = command.split(" : ")
    if course_name not in registered_dict:
        registered_dict[course_name] = []
    registered_dict[course_name].append(registered_student)
    command = input()

for course_name, registered_student in (sorted(registered_dict.items(), key=lambda x: len(x[1]), reverse=True)):
    print(f'{course_name}: {len(registered_student)}')
    registered_student_sorted = sorted(registered_student)
    for student in registered_student_sorted:
        print(f'-- {student}')
