def numbers_searching(*args):
    sequence = list(args)
    result = []
    for i in range(len(sequence)):
        if sequence.count(sequence[i]) >= 2:
            result.append(sequence[i])
    result = sorted(list(set(result)))

    min_sequence = min(sequence)
    max_sequence = max(sequence)
    new_sequence = []
    for i in range(min_sequence, max_sequence + 1):
        new_sequence.append(i)
    new_sequence = set(new_sequence)
    sequence = set(sequence)

    missing_element = new_sequence.difference(sequence)
    missing_element = list(missing_element)[0]
    final_result = [missing_element, result]
    return final_result


print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
