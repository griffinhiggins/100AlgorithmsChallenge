import re
def longestDigitsPrefix(txt):
    p = re.compile("^\d*")
    pre = p.search(txt)
    print(pre.group(0))



inputString="123aa1" 
longestDigitsPrefix(inputString)
# print(math.isnan("asdf"))
