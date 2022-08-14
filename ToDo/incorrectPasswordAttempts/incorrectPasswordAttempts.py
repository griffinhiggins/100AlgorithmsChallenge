def incorrectPasscodeAttempts(p,a):
    return len(list(filter(lambda e : e != passcode, attempts))) < 10
    
passcode = "1111" 
attempts = ["1111", "4444",
            "9999", "3333",
            "8888", "2222",
            "7777", "0000",
            "6666", "7285",
            "5555", "1111"]
print(incorrectPasscodeAttempts(passcode, attempts))
