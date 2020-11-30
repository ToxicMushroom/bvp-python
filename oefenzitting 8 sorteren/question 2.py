import random


def shuffle(list):
    for i in range(len(list)):
        j = random.randint(0, len(list) - 1)
        other = list[j]
        list[j] = list[i]
        list[i] = other

    return list


def ordered(list):
    last = list[0]
    for i in range(len(list)):
        if list[i] < last:
            return False
        else:
            last = list[i]
    return True


def shotgun_sort(list):
    while not ordered(list):
        shuffle(list)
    return list


lijst = [2, 3, 1, 0, 7, 8, 9]
print(shotgun_sort(lijst))
