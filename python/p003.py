# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

from math import sqrt
from time import clock

def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False

    # return False if n % i == 0
    return all(n % i for i in range(3, int(sqrt(n)) + 1, 2))

def max_prime_factor(n):
    N = int(sqrt(n)) + 1
    
    temp = N
    for i in range(N):
        if n%temp == 0:
            if (is_prime(n/temp)):
                return int(n/temp)
            if (is_prime(temp)):
                return temp
        temp-=1

t0 = clock()
print(max_prime_factor(600851475143))
print(clock() - t0)

# Based on the solution given
def max_prime_factor_solution(n):
    last_factor = 0
    if n % 2 == 0:
        last_factor = 2
        n = n / 2
        while n % 2 == 0:
            n = n / 2
    else:
        last_factor = 1

    factor = 3
    max_factor = sqrt(n)
    while n > 1 and factor <= max_factor:
        if n % factor == 0:
            n = n / factor
            last_factor = factor
            while n % factor == 0:
                n = n / factor
            max_factor = sqrt(n)
        factor = factor + 2

    if n == 1:
        return last_factor
    else:
        return n

t0 = clock()
print(max_prime_factor_solution(600851475143))
print(clock() - t0)
