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

# print(solution(2000000))


def solution2(N):
    L = int(sqrt(N))
    sieve = [False] * N
    for i in range(4, N, 2):
        sieve[i] = True

    for i in range(3, L, 2):
        if not sieve[i]:
            for j in range(i*i, N, 2*i):
                sieve[j] = True

    sum = 0
    for i in range(2, N):
        if not sieve[i]:
            sum = sum + i

    return sum

# print(solution2(2000000))


# Odd solution
def solution3(N):
    sievebound = int((N-1) /2)
    sieve = [False] * sievebound
    crosslimit = int((sqrt(N)-1) / 2)

    for i in range(1, crosslimit):
        if not sieve[i]:
            for j in range(2*i*(i+1), sievebound, 2*i+1):
                sieve[j] = True

    sum = 2
    for i in range(1, sievebound):
        if not sieve[i]:
            sum = sum + 2*i+1

    return sum

print(solution3(2000000))