def perfect_number(num: int):
    sum_divisors = 0
    for i in range(1, num + 1):
        if num % i == 0:
            sum_divisors += i
    if num == (sum_divisors / 2):
        return 'We have a perfect number!'
    else:
        return 'It\'s not so perfect.'


number = int(input())
print(perfect_number(number))

