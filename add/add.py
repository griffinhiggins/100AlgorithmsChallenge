def add(*args):
    try:
        return sum(int(i) for i in args)
    except:
        False

print(add(1,2))
print(add(1, 2));
print(add(3, 2));
print(add(1,2,3,4,5));
print(add(2,3));

