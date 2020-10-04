import math

radius = float(input('Enter a radius: '))

area_circle = radius**2 * math.pi
circumference_circle = radius*2 * math.pi

volume_sphere = 4/3 * math.pi * radius**3
area_sphere = 4 * math.pi * radius**2

print("area circle:", area_circle)
print("circumference circle:", circumference_circle)

print("volume sphere:", volume_sphere)
print("area sphere:", area_sphere)
