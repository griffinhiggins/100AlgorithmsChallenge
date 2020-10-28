def addBorder(a):
    r = len(a)
    c = len(a[0])
    wall = "".join("*"*(c+2))
    for i in range(r):
       a[i] = "*" + a[i] + "*"
    a.insert(0,wall)
    a.append(wall)
    return a

print(addBorder(["a"]));
print(addBorder(["abc", "ded"]));