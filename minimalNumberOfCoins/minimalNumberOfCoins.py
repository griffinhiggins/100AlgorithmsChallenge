def minimalNumberOfCoins(c,p):
    n = 0
    for i in reversed(c):
        if p == 0:
            break;
        while p > 0:
            if p // i > 0:
                p -= i
                n += 1
            else:
                break;
    return n

print(minimalNumberOfCoins([1, 2, 10],28))