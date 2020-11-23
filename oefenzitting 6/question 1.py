def main():
    if not m < n:
        print("read instructions you dummy")
        return
    even = set()
    div_three = set()
    for i in range(m, n + 1):
        if i % 2 == 0:
            even.add(i)
        if i % 3 == 0:
            div_three.add(i)
    div_six = set()
    for j in div_three:
        if j % 6 == 0:
            div_six.add(j)
    print("divisible by 6: ", len(div_six))
    print("divisible by 3: ", len(div_three))
    print("divisible by 2 or 3: ", len(even) + len(div_three))


m = int(input("m: "))
n = int(input("n (bigger than m): "))

main()
