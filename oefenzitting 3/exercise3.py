number = int(input("Enter a number: "))
total = 0
flipper = True

while number != 0:
    if flipper:
        total += number
        flipper = False
    else:
        total -= number
        flipper = True
    number = int(input("Enter a number: "))

print(total)
