def pigLatin(s):
    notCons = ['a', 'e', 'i', 'o', 'u', 'y']
    if s[0] in notCons:
        return s + 'way'
    i = 0
    for j in range(len(s)):
        if s[j] in notCons:
            i = j
            break;
    return  s[i:] + s[:i] + 'ay'
print(pigLatin("glove"))
print(pigLatin("eight"))