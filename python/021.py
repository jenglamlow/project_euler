from math import sqrt


# From Problem 12
def sum_of_divisor(n):
    sum = 0
    for i in range(1, int(sqrt(n))):
        if n % i == 0:
            sum += i
            if n / i != n:
                sum += n / i
    return sum


def answer(N):
    sum = 0
    for a in range(2, N):
        b = sum_of_divisor(a)
        if b > a:
            if sum_of_divisor(b) == a:
                sum += a + b

    return sum

print(answer(10000))


def improved_sum_of_divisor(n):
    sum = 1
    p = 2
    temp = n
    while p * p <= n and n > 1:
        if n % p == 0:
            j = p * p
            n = n / p
            while n % p == 0:   # divide prime factorization
                j = j * p
                n = n / p
            sum = sum * (j - 1)
            sum = sum / (p - 1)
        if p == 2:  # even
            p = 3
        else:       # odd + step size 2
            p += 2

    if n > 1:
        sum = sum * (n + 1)

    return sum - temp

