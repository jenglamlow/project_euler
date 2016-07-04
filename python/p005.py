# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def is_divisble(n):
    for p in range(2, 20):
        if n % p != 0:
            return False

    return True


def answer():
    n = 20
    while True:
        if is_divisble(n):
            return n
        n = n + 20

print(answer())

# Solution
# N = 2 * 3 * 2 * 5 * 7 * 2 * 3 * 11 * 13 * 2 * 17 * 19

# HackerRank
def is_divisible(n, N):
    for p in range(2, N):
        if n % p != 0:
            return False

    return True


def answer(N):
    n = N
    while True:
        if is_divisible(n, N):
            return n
        n = n + N
        
for _ in range(int(input())):
    print(answer(int(input())))

