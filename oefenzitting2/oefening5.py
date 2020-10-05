a = int(input("First number? "))
b = int(input("Second number? "))
c = int(input("Third number? "))

ls = [a, b, c]

list.sort(ls)
print(f"The inputs in sorted order are: {ls[0]}, {ls[1]} and {ls[2]}")
