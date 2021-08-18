movie = input()
total_standard = 0
total_student = 0
total_kid = 0
while movie != "Finish":
    seats = int(input())
    ticket = input()
    count_standard = 0
    count_student = 0
    count_kid = 0
    sold_tickets = 0
    while ticket != "End":
        sold_tickets += 1
        if ticket == "standard":
            count_standard += 1
        elif ticket == "student":
            count_student += 1
        elif ticket == "kid":
            count_kid += 1
        if sold_tickets == seats:
            break
        ticket = input()
    print(f'{movie} - {(count_standard + count_student + count_kid) / seats * 100:.2f}% full.')
    total_standard += count_standard
    total_student += count_student
    total_kid += count_kid
    movie = input()

total = total_student + total_standard + total_kid
print(f'Total tickets: {total}')
print(f'{total_student/total *100:.2f}% student tickets.')
print(f'{total_standard/total *100:.2f}% standard tickets.')
print(f'{total_kid/total *100:.2f}% kids tickets.')


