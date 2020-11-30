n = int(input("Enter the number of terms: "))

forCounter = 0
for i in range(1, n+1):
    forCounter += i

print("The sum of the first 10 natural numbers is", forCounter)

whileCounter = 0
whileItter = 0
while whileItter <= n:
    whileCounter += whileItter
    whileItter += 1

print("The sum of the first 10 natural numbers is", whileCounter)
