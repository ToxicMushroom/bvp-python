number = float(input("Input a floating-point number: "))

if number == 0:
    print("zero")
elif number > 0:
    if number < 1:
        print("small")
    elif number > 1000000:
        print("large")
    else:
        print("positive")
else:
    print("negative")



