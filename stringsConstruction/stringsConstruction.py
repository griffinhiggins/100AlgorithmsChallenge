def stringsConstruction(a,b):
    a = setStrCount(a)
    b = setStrCount(b)
    if not len(a) == len(b):
        return 0
    else:
        count = float('inf')
        for i in a:
            f = math.floor(b[i]/a[i])
            if f < count:
                count = f
    return count

def setStrCount(s):
    d = {}
    s_cp = "".join(set(s))
    for i in range(len(s_cp)):
        d[s_cp[i]] = s.count(s_cp[i])
    return d

print(stringsConstruction('abc','abccba'))