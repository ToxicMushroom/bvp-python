##
# This program calculates the perimeter and diameter of a letter 8.5 x 11
#

WIDTH = 8.5
HEIGHT = 11

perimeter = (WIDTH + HEIGHT) * 2
diagonal = (WIDTH**2 + HEIGHT**2)**0.5

print("Perimeter is {} inches.".format(perimeter))
print("Diagonal is {} inches.".format(diagonal))
