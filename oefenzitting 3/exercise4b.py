end = int(input("Enter number we will use 0-number range to scan for primes: "))

for prime in range(end + 1):
    divisions = 0
    for i in range(2, prime + 1):
        if prime % i == 0:
            divisions += 1
    if divisions == 1:
        print(prime)

