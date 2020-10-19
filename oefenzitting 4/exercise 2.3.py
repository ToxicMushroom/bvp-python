s = "aAabAcC"
# PRE: s elemt of string

amt = 0
len_string = len(s)
counter = 0

# invariant: counter <= len_string AND atm <= counter
while (counter != len_string):
    # counter < len_string AMD atm <= counter
    if s[counter].isupper():
        # counter < len_string AND atm <= (counter + 1)
        amt += 1
    counter += 1
    # counter <= len_string AND atm <= counter

# variant = len_string - counter
# counter = len_string AND atm <= counter
print(amt)