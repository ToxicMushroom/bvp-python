def eval1(coef, x):
    res = 0.0
    for i in range(0, len(coef)):
        term = float(coef[i])
        for j in range(0, i):
            term = term * x
        res = res + term
    return res
    # (n + n) * n + 1  | O(n^2)
    # (n + n) * 0 + 1  | O(n)
    # O(n^1,5) ??


def eval2(coef, x):
    res = 0.0
    term = 1.0
    for i in coef:
        res = res + term * i
        term = term * x
    return res
    # O(2n)


def eval3(coef, x):
    res = float(coef[-1])
    for i in range(len(coef) - 2, -1, -1):
        res = res * x + coef[i]
    return res
    # O(n)
