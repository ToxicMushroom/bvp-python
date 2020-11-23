def binary_search(lijst, value):  # returns index of value or -1
    index = -2
    start = 0
    end = len(lijst) - 1

    while index == -2:
        middle = start + ((end - start) // 2)
        print(middle)
        if end - start == 1:
            if lijst[end] == value:
                index = end
            elif lijst[start] == value:
                index = value
            else:
                index = -1

        if lijst[middle] == value:
            index = middle

        if value < lijst[middle]:
            end = middle
        else:
            start = middle
    return index


lijst = [5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 20]

for i in range(len(lijst)):
    el = lijst[i]
    print("searching ", el)
    print(i)
    print(binary_search(lijst, el))
