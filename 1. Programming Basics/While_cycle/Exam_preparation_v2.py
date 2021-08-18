bad_mark_count = int(input())
name_test = input()
mark = int(input())
sum_mark = 0
test_count = 0
count_bad_mark = 0
last_test = ''
is_failed = False
while name_test != "Enough":
    sum_mark += mark
    test_count += 1
    last_test = name_test
    if mark <= 4:
        count_bad_mark += 1
    if count_bad_mark == bad_mark_count:
        is_failed = True
        break
    name_test = input()
    mark = int(input())
average_score = sum_mark / test_count
if is_failed:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {test_count}')
    print(f'Last problem: {last_test}')
else:
    print(f'You need a break, {bad_mark_count} poor grades.')