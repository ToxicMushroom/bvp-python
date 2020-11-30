fibonStorage = {}


def fibon(n):
    if n < 3:
        return 1
    if fibonStorage.keys().__contains__(n):
        return fibonStorage[n]
    else:
        new = fibon(n - 1) + fibon(n - 2)
        fibonStorage[n] = new
        return new


fibonNumber = fibon(7)
print("fibon: ", fibonNumber)
print(fibonStorage)
