number = int(input("Enter number: "))

newNumber = 0
valid = True
multiplier = 1
size = 0

while (float(number) / multiplier) > 1:
    size += 1
    multiplier *= 10

multiplier = 1

while number > 0:
    if (number % (10 * multiplier)) == 0:
        multiplier *= 10
    else:
        number -= multiplier
        newNumber += (10 ** size) / (multiplier * 10)

print(newNumber)
