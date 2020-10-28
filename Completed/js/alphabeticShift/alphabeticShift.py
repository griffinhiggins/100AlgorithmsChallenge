def alphabeticShift(s):
    s = list(s)
    for i in range(len(s)):
        s[i] = "a" if ord(s[i]) % 122 == 0 else chr(ord(s[i]) + 1)
    return "".join(s)


print(alphabeticShift("crazy"))
