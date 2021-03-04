def quicksort(lijst):
    lengte = len(lijst)
    if lengte <= 1:
        return lijst


    pivot = lijst.pop()
    lengte -= 1
    lower_part = []
    higher_part = []
    equal_part = [pivot]
    for el in lijst:
        if el < pivot:
            lower_part.append(el)
        elif el == pivot:
            equal_part.append(el)
        else:
            higher_part.append(el)

    print(pivot)
    return quicksort(lower_part) + equal_part + quicksort(higher_part)


input = [1, 2, 3, 4, 5, 6, 6, 7, 8, 8, 5, 43, 23, 34, 3, 532, 535, 325, 5]
print(quicksort(input))
