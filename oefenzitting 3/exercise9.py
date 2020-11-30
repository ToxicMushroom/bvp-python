import math

height = int(input("Enter the height for the diamond star: "))

while height > 0:
    half = math.floor(height / 2.0)
    extra = (height - 2 * half) > 0
    for i in range(half):
        print((' ' * (half - i + extra - 1)) + ('*' * (1 + i * 2)))
    if extra:
        print('*' * height)
    for i in range(half):
        j = half - i - 1
        print((' ' * (half - j + extra - 1)) + ('*' * (1 + j * 2)))
    height = int(input("Enter the height for the diamond star: "))
