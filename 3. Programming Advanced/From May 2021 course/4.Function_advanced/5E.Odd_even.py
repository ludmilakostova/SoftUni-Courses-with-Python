def odd_even(string: str, expression: list):
    if key_word == "Odd":
        odd_seq = [el for el in expression if el % 2 == 1]
        print(sum(odd_seq)*len(expression))

    elif key_word == "Even":
        even_seq = [el for el in expression if el % 2 == 0]
        print(sum(even_seq) * len(expression))


key_word = input()
sequence = [int(el) for el in input().split()]
odd_even(key_word, sequence)
