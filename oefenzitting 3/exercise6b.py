positive = int(input("enter x: "))

som = 0
addition = 1

counter = 0
while addition > 0.001:
    factorial = 1
    for i in range(1, counter + 1):
        factorial *= i
    addition = (positive**counter)/factorial
    som += addition
    counter += 1

print(som)
