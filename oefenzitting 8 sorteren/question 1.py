import random


def list(lower, upper, length):
    lijst = []
    for i in range(length):
        lijst.append(random.randint(lower, upper))
    return lijst


def sorted_list(lower, upper, length):
    lijst = list(lower, upper, length)
    lijst.sort()
    return lijst


print(sorted_list(0, 50, 100))
