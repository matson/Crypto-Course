'''
Question 1 [15 points]

Select a secure hash function H and create its truncated version H' 
that outputs 32 bit digests. Implement a program that finds collisions in H' 
using the Rho method, starting from some random hash value. What is the size of the circle?
'''

#Picked: SHA-256.
#any from the SHA-2 Family is considered secure 
#evaluations should be up to 2^16+2^16 iterations average. (Does not have to be this number exactly)
#with the 32-bit digest.
#truncating a hash function make collisions more likely
#size of the circle is 341 (evaluations made).
import hashlib

def secure_Hash(h):
  if isinstance(h, str): #if it is a string, must convert to bytes.
    byte_hash = h.encode()
  return (hashlib.sha256(byte_hash).hexdigest()[:4])

def find_dem_Collisions():
  #find collisions, Rho Method.
  #starting with some random hash Value (H1) = H1'
  #compute H2 = Hash(H1) 
  #compute H2' = Hash(Hash(H1'))
  H1 = secure_Hash("hi there")
  H1prime = H1
  Hn = secure_Hash(H1)
  Hnprime = secure_Hash(secure_Hash(H1prime))
  i = 1
  while not(Hn == Hnprime):
    prevHash = Hn
    prevHashPrime = Hnprime
    Hn = secure_Hash(prevHash)
    Hnprime = secure_Hash(secure_Hash(prevHashPrime))
    i = i + 1
    print(i)
  print("collision occured")
  print("This is Hn:",Hn)
  print("This is Hnprime:",Hnprime)

def main():
  find_dem_Collisions()
main()
