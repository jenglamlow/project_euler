# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?
from math import sqrt


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False

    # return False if n % i == 0
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

def answer(N):
    if N == 1:
        return 2
    n = 3
    count = 1
    last_prime = 3
    while True:
        if is_prime(n):
            last_prime = n
            count = count + 1
        if count == N:
            return last_prime
        n = n + 2

print(answer(10001))