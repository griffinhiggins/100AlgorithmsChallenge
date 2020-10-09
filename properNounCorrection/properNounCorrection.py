def properNounCorrection(s):
    return s[0].upper() + s[1:].lower()

print(properNounCorrection("pARiS"))
print(properNounCorrection("John"))