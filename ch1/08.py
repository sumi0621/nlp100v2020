def cipher(string):
    ret = ""
    for i in range(len(string)):
        if str.islower(string[i]):
            ret += chr(219 - ord(string[i]))
        else:
            ret += string[i]
    
    return ret

print(cipher("aaAAbbBB"))