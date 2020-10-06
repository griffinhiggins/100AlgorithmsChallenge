def func(e):
    return len(e)

def sortByLength(a):
    a.sort(key=func)
    return a

print(sortByLength(['abc',"","aaa","a","zz"]))