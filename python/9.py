def answer():
    abc_sum = 1000
    for a in range(abc_sum/3):
        for b in range(abc_sum/2):
            c = abc_sum - a - b
            if a*a + b*b == c*c:
                return a*b*c

print(answer())