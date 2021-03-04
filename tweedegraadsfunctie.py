import math

# f(x) = 2x^2 + 5x - 1

a = int(input("geef waarde voor a: "))
b = int(input("geef waarde voor b: "))
c = int(input("geef waarde voor c: "))

discriminant = (b ** 2) - 4 * a * c
x1 = (-b + discriminant ** 0.5) / (2 * a)
x2 = (-b - discriminant ** 0.5) / (2 * a)

print(x1, x2)

# check
y1 = a * math.pow(x1, 2) + b * x1 + c
y2 = a * math.pow(x2, 2) + b * x2 + c

print(y1, y2)
