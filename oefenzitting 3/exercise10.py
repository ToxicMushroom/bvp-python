arr = []
number = input()

first = True
while number != "q":
    getal = int(number)
    if first:
        arr.append(getal)
        first = False
    else:
        count = 0
        inserted = False
        for s in arr:
            if not inserted and s > getal:
                arr.insert(count, getal)
                inserted = True
            else:
                count += 1
        if not inserted:
            arr.append(getal)
    number = input()

print(arr)
