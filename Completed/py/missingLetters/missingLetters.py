def missingLetters(s):
    if not s[0] == 'a':
        return 'a'
    for i in range(1,len(s)):
        x = ord(s[i - 1])
        y = ord(s[i]) 
        if x < y  - 1:
            return chr(x + 1)
    return None
print(missingLetters("abce"))
print( missingLetters("abcdefghjklmno"))
print(missingLetters("abcdefghijklmnopqrstuvwxyz"))