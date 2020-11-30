positive = int(input("integer to calculate factorial of: "))

factorial = 1
for i in range(1, positive + 1):
    factorial *= i

print(factorial)