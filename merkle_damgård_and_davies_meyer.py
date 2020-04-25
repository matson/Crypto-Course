'''
(a) [10 points] Implement a M-D hash H based on the D-M compression that uses a secure block cipher. 
(b) [20 points] Implement a secret-prefix MAC based on H from the previous step. 
NOTE: I did not implement the padding that should be part of the merkle-damgard construction.
I used AES-128 as my "E" PRP for my compression function which is the Davies-Meyer construction. 
'''
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import re

def chunkstring(string, length):
  return re.findall('.{%d}' % length, string)

def convert_to_Bits(string):
  demBits = str.encode(string)
  return demBits

def bytes_to_Int(bytes):
  result = 0
  for b in bytes:
    result = result * 256 + int(b)
  #print("Converted into ints:",result)
  return result

#Converts ints to bytes.
def int_to_Bytes(value, length):
  result = []
  for i in range(0, length):
      result.append(value >> (i * 8) & 0xff)
  result.reverse()
  bytearr = (bytes(result))
  return bytearr

#E is AES-128.
def block_Cipher_E(mi,pH):
  cipher = AES.new(mi, AES.MODE_CBC) 
  IVA = cipher.iv #nonce
  ciphered_data = cipher.encrypt(pad(pH,AES.block_size)) 
  cipher = AES.new(mi, AES.MODE_CBC, iv=IVA) 
  ciphered_data = cipher.encrypt(pad(pH,AES.block_size)) 
  print("AES in the works...")
  return ciphered_data

def XOR(pH, result):
  #need to ints to XOR
  int_pH = bytes_to_Int(pH)
  int_result = bytes_to_Int(result)
  print("We XORED!")
  return int_pH ^ int_result

#compression Function 
#Hi = E(Mi, Hi-1) xor Hi-1
def compress(mi,pH):
  E = block_Cipher_E(mi,pH)
  final_Bytes = XOR(E, pH)
  new_Chaining = int_to_Bytes(final_Bytes, 16)
  return new_Chaining

def function_H(m,hi):
  hiString = hi.decode()
  joined = ''.join((hiString,m))
  #prepend at the beg. of M
  N = chunkstring(joined,16)
  M1 = convert_to_Bits(N[0])
  M2 = convert_to_Bits(N[1])
  M3 = convert_to_Bits(N[2])
  M4 = convert_to_Bits(N[3])
  #splits the message into blocks of identical size
  #takes an internal state H0
  #final value is the message's hash value
  H1 = compress(M1,hi)
  print("This is H1:",H1)
  H2 = compress(M2,H1)
  print("This is H2:",H2)
  H3 = compress(M3,H2)
  print("This is H3:",H3)
  H4 = compress(M4,H3)
  print("This is H4:", H4)
  return H4
#Secret-Prefix: 
#normal hash function into a keyed hash
#Prepend key to message
#return Hash(K || M)
  
def main():
  #message block M/Mi (usually 512 bits)
  #The Mis must be 128 bits in length:
  M = "Chocolate chip cookies from Insomnia, are the best in the world."
  #Internal state (IV) 
  H0 = b"secret"
  hashFinal = function_H(M,H0)
  print(hashFinal)
main()
