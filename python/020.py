import math


def sum_of_digit(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print(sum_of_digit(math.factorial(100)))