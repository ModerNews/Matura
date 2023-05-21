import math


def check_prime(n: int):
    if n in (0,1):
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def eratosthenes_sieve(n: int):
    primes = [True if i not in [0,1] else False for i in range(n)] # Wypełnia tablicę wartościami True dla każdej z liczb od 0 do n
    if n in [0, 1]:
        return primes
    for i in range(2, int(math.sqrt(n)) + 1):
        if primes[i]:
            tmp = i ** 2
            while tmp < n:
                primes[tmp] = False
                tmp += i
    return primes
