def bubble_sort(lijst):
    gesorteerd = False
    if len(lijst) < 2:
        return
    while not gesorteerd:
        previous = lijst[0]
        i = 0
        cancel = False

        while not cancel:
            if previous > lijst[i]:
                lijst[i - 1] = lijst[i]
                lijst[i] = previous
                cancel = True

            previous = lijst[i]
            i = i + 1
            if i == len(lijst) and not cancel:
                gesorteerd = True
                cancel = True
        print(lijst)
    return lijst


print(bubble_sort([2434, 4324324, 65, 64, 654, 7, 6, 43, 5, 7, 9, 3, 3, 23, 223, 46, 6, 6, 8, 854, 43]))
