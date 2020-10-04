# carthesiaanse coordinaten naar poolcoördinaten
import math

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

# math.atan returns in radialen
theta = math.degrees(math.atan(x/y))
radius = math.sqrt(x**2 + y**2)

print("The radius is:", radius)
print("Theta is:", theta)
