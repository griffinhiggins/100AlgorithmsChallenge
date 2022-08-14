def isLucky(n):
    n = str(n)
    MID = len(n)//2
    return sum([int(i) for i in n[:MID]]) == sum([int(i) for i in n[MID:]])
    
n = 1230
print(isLucky(n))
n = 239017
print(isLucky(n))
