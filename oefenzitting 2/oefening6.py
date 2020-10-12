grade = input("Enter letter grade? ")
letter = grade[0:1]
sign = grade[1:]
value = 0.0

if letter == "A":
    value = 4.0
elif letter == "B":
    value = 3.0
elif letter == "C":
    value = 2.0
elif letter == "D":
    value = 1.0
elif letter == "F":
    value = 0

if sign == "+":
    value += 0.3
elif sign == "-":
    value -= 0.3
if value > 4:
    value = 4
elif value <= 0.3:
    value = 0

print(f"Numeric value: {value}")
