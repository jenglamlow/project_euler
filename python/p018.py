
matrix = []

with open("p018_triangle.txt") as file:
    for line in file:
        line_list = [int(i) for i in line.split()]
        matrix.insert(0, line_list)


def answer(M):
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

# print(answer(matrix[:]))


def answer2(M):
    for i in range(len(M)-1):
        for j in range(len(M[i])-1):
            M[i+1][j] += max(M[i][j],M[i][j+1])

    return(M[len(M)-1][0])

# print(answer2(matrix[:]))


def maximum(M):
    for i in range(len(M[0])-1):
        M[1][i] += max(M[0][i], M[0][i+1])

    del M[0]

    if len(M) != 1:
        return maximum(M)
    else:
        return M[0][0]

print(maximum(matrix[:]))
