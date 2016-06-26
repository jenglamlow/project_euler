
M = []

with open("p067_triangle.txt") as file:
    for line in file:
        line_list = [int(i) for i in line.split()]
        M.insert(0, line_list)


def answer():
    sum_left = 0
    sum_right = 0

    while len(M) > 1:
        temp = []
        for j in range(len(M[0])-1):
            sum_left = M[0][j] + M[1][j]
            sum_right = M[0][j+1] + M[1][j]
            temp.append(max(sum_left, sum_right))
        del M[0:2]
        M.insert(0, temp)

    return(M[0][0])

print(answer())

# Refer to Problem 18 python for better solution
