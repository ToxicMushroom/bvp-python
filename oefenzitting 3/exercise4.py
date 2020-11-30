prime = int(input("Enter a prime number: "))

divisions = 0
for i in range(2, prime + 1):
    if prime % i == 0:
        divisions += 1

print(divisions)
