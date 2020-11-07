def calculate_sum_until(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum


total = calculate_sum_until(100)
print("total: ", total)
