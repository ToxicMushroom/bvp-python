def count_doubles(list):
    dict = {}
    doubles = []
    for i in range(len(list)):
        el = list[i]
        if el in dict and dict[el] == 1:
            doubles.append(list[i])
            dict[el] = 2
        else:
            dict[el] = 1
    return doubles


print(count_doubles([1, 2, 2]))


