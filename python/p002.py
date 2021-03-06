# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
L = 4000000


# Generator Method
def fibonacci():
    a, b = 1, 2
    while True:
        yield a
        a, b = b, a + b

sum = 0
for i, f in enumerate(fibonacci()):
    if f < L:
        if f % 2 == 0:
            sum += f
    else:
        break

print(sum)

# Loop Method
sum = 0
a = 1
b = 1
while b < L:
    if b % 2 == 0:
        sum += b
    temp = a + b
    a = b
    b = temp
print(sum)

# Loop Method (Every third Fibonacci is even)
sum = 0
a = 1
b = 1
c = a + b
while b < L:
    sum += c
    a = b + c
    b = c + a
    c = a + b
print(sum)

# Even Fibonacci Sequence F(n) = 4F(n-3) + F(n-6)
# Recursive
def r_even_fibonacci(n):
    if (n == 0):
        return 2
    elif (n ==  1):
        return 8
    return 4*r_even_fibonacci(n-1) + r_even_fibonacci(n-2)

F = 0
i = 0
sum = 0
while True:
    F = r_even_fibonacci(i)
    if F > L:
        break
    i += 1
    sum += F
print(sum)

# Pass Hacker Rank Test Cases
T = int(input())

cache = {}
def r_even_fibonacci(n):
    if (n == 0):
        return 2
    elif (n ==  1):
        return 8
    elif cache.get(n) != None:
        return cache.get(n)
    return 4*r_even_fibonacci(n-1) + r_even_fibonacci(n-2)

for i in range(T):
    N = int(input())
    F = 0
    i = 0
    sum = 0
    while True:
        F = r_even_fibonacci(i)
        cache[i] = F
        if F > N:
            break
        i += 1
        sum += F
    print(sum)
