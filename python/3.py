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
