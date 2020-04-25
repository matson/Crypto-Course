'''
Question 4 [20 points]

Implement a CBC-MAC based on AES-128. Using your program, 
generate two random message M1 and M2 and compute the corresponding tags T1 and T2. 
NOTE: Not the best way to split message blocks. I still struggle with this concept a 
little and still have to work to find a faster way to do so.
'''
#block-cipher used: AES-128.
#need an IV.
#generate random keys
#need XOR operations.

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random
import string
import os
import re

#generate messages
def make_Message(size):
    message = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    return message

#break message blocks
def chunkstring(string, length):
  return re.findall('.{%d}' % length, string)

def bytes_to_Int(bytes):
  result = 0
  for b in bytes:
    result = result * 256 + int(b)
  #print("Converted into ints:",result)
  return result

def int_to_Bytes(value, length):
  result = []
  for i in range(0, length):
      result.append(value >> (i * 8) & 0xff)
  result.reverse()
  bytearr = (bytes(result))
  return bytearr

#XOR
def XOR(m, n):
  #need to ints to XOR
  mInt = bytes_to_Int(m)
  nInt = bytes_to_Int(n)
  print("We XORED!")
  return mInt ^ nInt

#E AES-128
def block_Cipher(k,m):
  cipher = AES.new(k, AES.MODE_CBC) 
  IVA = cipher.iv #nonce
  ciphered_data = cipher.encrypt(pad(m,AES.block_size)) 
  cipher = AES.new(k, AES.MODE_CBC, iv=IVA) 
  ciphered_data = cipher.encrypt(pad(m,AES.block_size)) 
  print("AES in the works...")
  return ciphered_data

#T = MAC(K, M)
#create the Tag T:
def cbc_Mac(k,m,iv):
  sm = chunkstring(m, 16)
  #split message blocks
  m1 = sm[0]
  m2 = sm[1]
  m1Bytes = m1.encode()
  m2Bytes = m2.encode()
  mix1 = XOR(iv, m1Bytes) #first iv XOR operation
  mixB = int_to_Bytes(mix1,32)
  keyB = int_to_Bytes(k,16) #convert to bytes
  #turn all values to bytes for E-block
  #chaining:
  result1 = block_Cipher(keyB,mixB) #bytes
  mix2 = XOR(result1, m2Bytes) #ints
  result2 = int_to_Bytes(mix2,32) #bytes
  tag = block_Cipher(keyB,result2)
  return tag

def forgery():
  #apply CBC-MAC to M1 || (M2 exor T1)
  #compute C1 = E(K, M1) = T1 followed by:
  #C2 = E(K, (M2 exor T1) exor T1) = E(K, M2) = T2

def main():
  iv1 = os.urandom(16)
  iv2 = os.urandom(16)
  K1 = random.getrandbits(128)
  K2 = random.getrandbits(128)
  M1 = make_Message(32)
  M2 = make_Message(32)
  print("This is message 1:", M1)
  print("This is message 2:", M2)
  T1 = cbc_Mac(K1, M1, iv1)
  T2 = cbc_Mac(K2, M2, iv2)
  print("This is tag 1:", T1)
  print("This is tag 2:", T2)
main()
