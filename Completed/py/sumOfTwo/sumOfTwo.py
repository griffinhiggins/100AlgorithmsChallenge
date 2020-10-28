def sumOfTwo(a,b,v):
    for i in a:
        for j in b:
            if i + j == v:
                return True
    return False

print(sumOfTwo([1, 2, 3],[10, 20, 30, 40],42))