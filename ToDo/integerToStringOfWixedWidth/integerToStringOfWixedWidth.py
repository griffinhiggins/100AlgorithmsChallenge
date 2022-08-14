def integerToStringOfFixedWidth(n,w):
    n = str(n)
    LEGNTH = len(n)
    if w > LEGNTH: 
        return f"{'0' * (w - LEGNTH)}{n}"
    elif w < LEGNTH:
        return n[-w:]
    return n
        
        

    
number = 1234
width = 2
print(integerToStringOfFixedWidth(number, width))
# = "34";

number = 1234 
width = 4
print(integerToStringOfFixedWidth(number, width))
# = "1234";

number = 1234 
width = 5
print(integerToStringOfFixedWidth(number, width))
# = "01234".
