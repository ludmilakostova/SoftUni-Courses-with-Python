bad_marks_threshold = int(input())
count_bad_marks = 0
count_test = 0
total_mark_test = 0
last_test = ''
has_failed = True
while count_bad_marks != bad_marks_threshold:
    name_test = input()
    if name_test == "Enough":
        has_failed = False
        break
    mark_test = int(input())
    if mark_test <= 4:
        count_bad_marks +=1
    count_test += 1
    total_mark_test += mark_test
    last_test = name_test
average_mark = total_mark_test / count_test
if has_failed:
    print(f'You need a break, {count_bad_marks} poor grades.')
else:
    print(f'Average score: {average_mark:.2f}')
    print(f'Number of problems: {count_test}')
    print(f'Last problem: {last_test}')
