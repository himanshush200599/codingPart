def CCE(string,key):
    key = key%26  #if key value is higher than  26 the we will get the same number
    newString = ""
    for letter in string:
        character = ord(letter)+key
        if character>126:  #If ascii of z+4 we get invalid charcter so we take  modulo to take b
            character = 96+character%126
        newChar = chr(character)
        newString+=newChar
    return newString

print(CCE("abc",54))
