# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

from math import sqrt


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False

    # return False if n % i == 0
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))


def answer(N):
    total = 0;
    for n in range(2, N):
        if is_prime(n):
            total += n

    return total

# print(answer(2000000))

# Solution (Sieve of Eratosthenes)


def solution(N):
    L = N + 1
    sieve = [False] * L
    primes = []

    # mark even numbers > 2
    for i in range(2, L):
        if sieve[i]:
            continue
        for j in range(i*2, L, i):
            sieve[j] = True

        primes.append(i)

    return sum(primes)

print(solution(2000000))

