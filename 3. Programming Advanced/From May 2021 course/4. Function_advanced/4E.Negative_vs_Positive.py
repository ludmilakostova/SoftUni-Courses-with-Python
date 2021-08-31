def negative_vs_positive(expression: list):
    positive_num = [el for el in expression if el >= 0]
    negative_num = [el for el in expression if el < 0]
    sum_neg_num = sum(negative_num)
    sum_pos_num = sum(positive_num)
    print(sum_neg_num)
    print(sum_pos_num)
    if abs(sum_neg_num) > sum_pos_num:
        print(f'The negatives are stronger than the positives')
    else:
        print(f'The positives are stronger than the negatives')


sequence = [int(el) for el in input().split()]
negative_vs_positive(sequence)
