def pagesNumberingWithInk(c,n):
    while True:
        n -= len(str(c))
        if not (n - len(str(c)) + 1) > 0:
            return c
        c += 1
print(pagesNumberingWithInk(1,5))
print(pagesNumberingWithInk(21,5))
print(pagesNumberingWithInk(8,4))