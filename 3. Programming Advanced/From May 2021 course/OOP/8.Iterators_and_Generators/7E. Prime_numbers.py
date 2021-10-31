def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def get_primes(list_integers):
    primes = filter(lambda n: is_prime(n), list_integers)
    for num in primes:
        yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
