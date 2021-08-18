n = int(input())
positive_nums = []
negative_nums = []
for _ in range(n):
    current_number = int(input())
    if current_number >= 0:
        positive_nums.append(current_number)
    else:
        negative_nums.append(current_number)
print(positive_nums)
print(negative_nums)
print(f'Count of positives: {len(positive_nums)}. Sum of negatives: {sum(negative_nums)}')


