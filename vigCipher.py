#Implement the Vigenere decryption and provide 5 ptxt/ctxt pairs to demonstrate its correctness 

#1).Come up with key and plaintext

#provide 5 key-value pairs for Decrypt.
plainText = "CRYPTO" #plaintext
key = "DUH" #KEY 
cipherText = [] #new ciphertext
#should be FLFSNV.
def encrypt(plainText, key):
    keynum = [ord(i) for i in key] #convert to ASC. values
    keylen = len(key) #key length
    plainTextnum = [ord(i) for i in plainText] #conversion
    cipherText = [] #new ciphertext
    #2). Go through all chars. in string
    for i in range(len(plainTextnum)): #indices must be an integer
        x = (plainTextnum[i] + keynum[i % keylen]) % 26 #loop around
        cipherText.append(chr(x+65)) #need to expand range to get to 65 
    #return cipherText
    print(cipherText)

encrypt(plainText, key)

cipher = "FLFSNV" #should be CRYPTO
#key define above
cipher1 = "ICPMM" #should be HELLO
key1 = "BYEBY"
cipher2 = "WBLBXYLHRWBLWYH" #should be They drink the tea.
key2 = "DUH"
cipher3 = "WRIV" #should be EVER
key3 = "SWEE"
cipher4 = "KYVL" #should be OURS
key4 = "WEET"

def keyLen(key):
  keylen = len(key)
  return keylen
#returns keylength

def decrypt(cipher, key):
    keynum = [ord(i) for i in key] #convert to ASC. values
    keylen = keyLen(key) #key length generator
    cipherTextnum = [ord(i) for i in cipher] #conversion
    newText = [] #new ciphertext
    #2). Go through all chars. in string
    for i in range(len(cipherTextnum)): #indices must be an integer
        x = (cipherTextnum[i] - keynum[i % keylen]) % 26 #loop around
        newText.append(chr(x+65)) #need to expand range to get to 65 
    #return newText
    print(newText)

decrypt(cipher4, key4) #change key-value pairs here.