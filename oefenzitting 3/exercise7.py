credit_card = input("enter credit card: ")
length = len(credit_card)

firstArr = []
secondArr = []

for i in range(0, length):
    if i % 2 == 1:
        firstArr.append(int(credit_card[i]))
    else:
        second = str(int(credit_card[i]) * 2)
        for j in range(len(second)):
            secondArr.append(int(second[j]))

som = 0
for item in firstArr:
    som += item
for item in secondArr:
    som += item

if som % 10 > 0:
    print("invalid")
else:
    print("valid")
