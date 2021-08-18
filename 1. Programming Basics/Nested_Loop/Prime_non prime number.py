command = input()
sum_prime = 0
sum_non_prime = 0
while command != "stop":
    num = int(command)
    is_prime = True
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
    elif num < 0:
        print(f'Number is negative.')

    if is_prime and num > 1:
        sum_prime += num
    if not is_prime and num >1:
        sum_non_prime += num
    command = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
