def newNumeralSystem(n):
    rv = []
    a = ord('A')
    n = ord(n) - a;
    for i in range(n // 2 + 1):
        rv.append(chr(i + a) + " + " + chr(n + a))
        n -= 1
    return rv

print(newNumeralSystem('A'))
print(newNumeralSystem('E'))
print(newNumeralSystem('G'))