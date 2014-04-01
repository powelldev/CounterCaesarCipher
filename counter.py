import enchant

dictionary = enchant.Dict("en_US")

# Get ciphertext
# Decipher with a key
# Check for spaces, if spaces, tokenize.
    # possible result, present
    # spell check result, if successful, present

def decipher(key, message):
    def addkey(character):
        temp = ord(character) + key
        if (temp == 32 + key):
            temp = 32
        elif (temp > 122):
            temp = temp - 26
        elif (temp < 97):
            temp = temp + 26
        return temp
    nctxt = map (addkey, message)
    ptxt = map (chr, nctxt)
    return ptxt
    
ciphertext = "wklv lv d vhfuhw phvvdjh"

for key in range(0, 26):
    ptext = ''.join(decipher(key, ciphertext))
    x = ptext.split()
    for token in x:
        if (token.__len__() <= 1): continue
        elif (dictionary.check(token) == True):
            print ptext
            break


#    if spellcheck(plaintext):
#        print plaintext
