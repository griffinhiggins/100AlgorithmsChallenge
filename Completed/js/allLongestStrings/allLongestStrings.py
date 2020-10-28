def allLongestStrings(a):
    ret = []
    longest = 0
    for i in range(len(a)):
        if(longest < len(a[i])):
            longest = len(a[i])
    for i in range(len(a)):
        if(longest == len(a[i])):
            ret.append(a[i])
    return ret


print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))
