command = input()
sum_prime = 0
sum_other = 0
while command != 0:
    num = int(command)

    if num < 0:
        print(f'Number is negative.')
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                sum_other += num
            else:
                sum_prime += num
    command = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_other}')
