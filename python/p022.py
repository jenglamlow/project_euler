name_list = []

with open("p022_names.txt") as file:
    for line in file:
        for word in line.split(","):
            name_list.append(word.replace("\"", ""))

name_list.sort()


def answer(namelist):
    score = 0
    count = 1
    for name in namelist:
        score += ((sum(bytearray(name)) - 64 * len(name)) * count)
        count += 1

    return score

print(answer(name_list))

