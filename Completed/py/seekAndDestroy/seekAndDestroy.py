def seekAndDestroy(a,b):
    c = []
    for i in a:
        if not i in b:
            c.append(i)
    return c


print(seekAndDestroy([3, 5, 1, 2, 2], [2, 3, 5]))
print(seekAndDestroy([1, 2, 3, 5, 1, 2, 3], [2, 3]))
