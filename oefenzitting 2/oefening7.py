first = float(input("Enter a floating-point number: "))
second = float(input("Enter a floating-point number: "))

diff = 0.0
if first > second:
    diff = first - second
else:
    diff = second - first

if diff >= 0.01:
    print("They are different.")
else:
    print("They are the same up to two decimal places.")
