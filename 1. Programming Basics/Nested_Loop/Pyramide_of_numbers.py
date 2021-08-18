n = int(input())
counter = 1
is_counter_bigger_than_n = False

for row in range(1, n + 1):
    for column in range(1, row + 1):
        if counter > n:
            is_counter_bigger_than_n = True
            break
        print(counter, end=" ")
        counter += 1
    if is_counter_bigger_than_n:
        break
    print()
