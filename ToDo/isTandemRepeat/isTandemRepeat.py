def isTandemRepeat(txt):
    LENGTH = len(txt)
    return False if LENGTH % 2 != 0 else txt[0:LENGTH//2] == txt[LENGTH//2:]

inputString = "tandemtandem"
print(isTandemRepeat(inputString))
inputString = "qqq"
print(isTandemRepeat(inputString))
inputString = "2w2ww"
print(isTandemRepeat(inputString))
