def square_of_sum(N):
    return ((N * (1 + N)) / 2) ** 2


def sum_of_square(N):
    return (N * (N + 1) * (2*N + 1))/6


def answer(N):
    return square_of_sum(N) - sum_of_square(N)


print(answer(100))