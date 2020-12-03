def maximum(a):
    i = 0  # AT
    max = a[i]  # AT
    while i < len(a):
        if a[i] > max:  # AV
            max = a[i]  # AT
        i = i + 1  # AT
    # n iteraties
    # 3n+2 O(n)
