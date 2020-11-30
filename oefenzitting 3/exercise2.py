degrees = input("enter degrees: ")
farenheit = []

while degrees != "q":
    celcius = float(degrees)
    farenheit.append(celcius * 9/5 + 32)
    degrees = input("enter degrees: ")

print(farenheit)
