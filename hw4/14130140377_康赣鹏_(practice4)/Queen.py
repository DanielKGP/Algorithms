def place(x, k):
    for i in range(1, k):
        if x[i] == x[k] or abs(x[i] - x[k]) == abs(i - k):
            return False
    return True
def queens(n):
    k = 1
    x = [0 for row in range(n + 1)]
    while k > 0:
        x[k] = x[k] + 1
        while (x[k] <= n) and (not place(x, k)):
            x[k] = x[k] + 1
        if x[k] <= n:
            if k == n:
                break
            else:
                k = k + 1
                x[k] = 0
        else:
            x[k] = 0
            k = k - 1
    return x[1:]

print(queens(8))
