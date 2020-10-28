def palindromeRearranging(s):
    sList = list(s)
    sSet = set(s)
    oddCount = 0
    for i in sSet:
        if sList.count(i) % 2 == 1:
            oddCount += 1
            if oddCount > 1:
                return False
    return True
        

print(palindromeRearranging("a"))
print(palindromeRearranging("ab"))
print(palindromeRearranging("aaabbb"))
print(palindromeRearranging("aabb"))
