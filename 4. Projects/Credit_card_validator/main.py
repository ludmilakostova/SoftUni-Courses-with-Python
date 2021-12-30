cc_num = input("Please enter your credit card number: ")

"""Elimination of the whitespaces if any exist during the input"""
cc_num = cc_num.replace(" ", "")
even_num = []
odd_num = []

"""Separation of the digits by even and odd positions"""
for i in range(len(cc_num)):
    if i % 2 == 0:
        even_num.append(cc_num[i])
    else:
        odd_num.append(cc_num[i])

"""Each even digit is doubled. If the result is a double digit, it needs
to be simplified to one digit"""
even_num_double = []
for i in range(len(even_num)):
    even_num_double.append(int(even_num[i]) * 2)

result_even = []
for i in range(len(even_num_double)):
    if even_num_double[i] >= 10:
        el = str(even_num_double[i])
        mid_res = int(el[0]) + int(el[1])
        result_even.append(mid_res)
        continue
    result_even.append(even_num_double[i])

result_odd = [int(el) for el in odd_num]

"""Sum of all even digits and odd ones. If the result is divisible by 10, the card number is valid"""
final_result = sum(result_even) + sum(result_odd)
if final_result % 10 == 0:
    print(f'Valid credit card number')
else:
    print(f'Invalid credit card number')
