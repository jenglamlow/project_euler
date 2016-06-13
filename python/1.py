# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Looping method
print(sum([x for x in range(1000) if x%3==0 or x%5==0]))


# Mathematics method
# an = a1 + (n-1)d
# 3 + 6 + 9 + 12 = 3(1 + 2 + 3 + 4...)
# 5 + 10 + 15 + 20 = 5(1 + 2 + 3 + 4...)
# an = 1 + (n-1)(1) = n
# Sn = n(a1 + an)/2
# Sn = d*n(1 + n)/2

N = 1000

def sum_divisible_by(d):
    n = (N - 1) / d
    return (d*n*(1+n))/2
print(sum_divisible_by(3) + sum_divisible_by(5) - sum_divisible_by(15))
