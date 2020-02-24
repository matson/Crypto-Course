#Semanitcally Secure Cipher

import random 
import string
#Semanitcally Secure Cipher

#Need 5 pairs ctxt/ptxt
#pair 1
plainText1 = "Hello!"
key1 = "duh" #confirmed
#pair 2
plainText2 = "cold weather"
key2 = "fhtg"
#pair 3
plainText3 = "chocolate" 
key3 = "eyhthgf"
#pair 4
plainText4 = "butter"
key4 = "thfbhh"
#pair 5
plainText5 = "hi there!"
key5 = "ght"

cipherText = ""


#use XOR operation 
def xor(X, Y): 
  return "".join([chr(ord(a) ^ ord(b)) for (a, b) in zip(X, Y)])

#Uses a deterministic random bit generator (DRBG)
#https://pynative.com/python-generate-random-string/
#https://docs.python.org/3/library/random.html
def generator():
  random.seed(a=None, version=2)
  value = string.ascii_lowercase
  stuff = ''
  for i in range(10):
    stuff += stuff.join(random.choice(value))
    
  print("this is stuff:", stuff)#works
  return stuff
Stuff = generator()
#print(Stuff)

newKey = key2 + Stuff #add the randoms to the key (K + R)/change key here
print("this is the newKey:", newKey)

#again
def generator2(p):
  random.seed(a=newKey, version=2)
  cookie = string.ascii_lowercase
  Blah = ''
  for i in range(len(plainText2)):
    Blah += Blah.join(random.choice(cookie))
    
  print("This is Blah:", Blah)#works
  return Blah
BLAH = generator2(plainText2)
#print(BLAH)

#will take in testing key and chosen plaintext
def encrypt(p):
  #E(K, R, P) = (DRBG(K R) ⊕ P, R)
  cipherText = xor(BLAH, p) #xor function used
  final = Stuff + cipherText #final combined cipherText
  print("this is the final:", final)
  return final
finalText = encrypt(plainText2)#should work?
#print(finalText)

def decrypt(c):
  brownies = c[0:10] #first 10 elements
  keyNew = key2 + brownies #change 
  random.seed(keyNew)#like previous case
  burger = string.ascii_lowercase
  transform = ""
  for i in range(len(c)):
    transform += transform.join(random.choice(burger))
  plainText = xor(c[10:], transform)#xoring back 
  
  #print("this is the regular text:", plainText)
  return(plainText)

plain = decrypt(finalText)
print(plain)
#Last step to see if the plainText comes back normal




