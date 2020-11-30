n = int(input("n: "))
# PRE: n elemt van N

counter = 0
fact = 1

# invariant: counter <= n AND fact = counter!
while counter != n:
    # counter < n AND fact = counter!
    counter = counter + 1
    # counter <= n AND fact = (counter-1)!
    fact = fact * counter
    # counter <= n AND fact = (counter-1)! * counter = counter!
# Variant: n - counter


# END
# counter = n
# fact = counter! = n!

# POST: fact = n!
print("fact: ", fact)
