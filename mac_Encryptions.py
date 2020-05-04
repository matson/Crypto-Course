'''
Question 1 [40 points total - answer all parts]

Using crypto libraries in a secure way:

(a) [10points] Implement EaM using Simon128/128-CTR as the cipher and Poly1305-AES as the MAC. Your implementation should support multiple plaintext blocks.

(b) [15points] Implement MtE using Speck128/128-CBC (with a random IV) as the cipher and HMAC-SHA-256 as the MAC. Your implementation should support multiple plaintext blocks.

(c) [15points] Implement EtM using Simon128/256-CTR as the cipher and AES-CMAC as the MAC. Your implementation should support multiple plaintext blocks.

**Note: SimonX/Y indicates block size X and key size Y. The same applies to SpeckX/Y.
'''
import random
import string
import os
import hmac
from simon import SimonCipher
from speck import SpeckCipher
from Crypto.Hash import Poly1305
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Hash import CMAC

#generate messages
def make_Message(size):
    message = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])
    return message

#bytes to ints.
def bytes_to_Int(bytes):
  result = 0
  for b in bytes:
    result = result * 256 + int(b)
  #print("Converted into ints:",result)
  return result

#ints to bytes.
def int_to_Bytes(value, length):
  result = []
  for i in range(0, length):
      result.append(value >> (i * 8) & 0xff)
  result.reverse()
  bytearr = (bytes(result))
  return bytearr

#CTR mode: 
def simon128_Cipher(k,p):
  #set by default to 128 bit size...no specifications.
  ctr_cipher = SimonCipher(k, mode='CTR', init=0xCABCABCAB, counter=1)
  simon_ciphertext = ctr_cipher.encrypt(p)
  return simon_ciphertext

#CBC mode:
def speck128_Cipher(k,iv,p):
  #set by default to 128 bit size...
  cbc_cipher = SpeckCipher(k, mode='CBC', init=iv)
  speck_cbc_ciphertext = cbc_cipher.encrypt(p)
  return speck_cbc_ciphertext

def simon128_256_Cipher(k,p):
  #simon128/256-CTR
  ctr_cipher = SimonCipher(k, mode='CTR', init=0xCABCABCAB, counter=1,key_size=256, block_size=128)
  simon_ciphertext = ctr_cipher.encrypt(p)
  return simon_ciphertext

#AES MAC:
def poly1305(k,p):
  #secret = b'Thirtytwo very very secret bytes'
  mac = Poly1305.new(key=k, cipher=AES)
  mac.update(p)
  tag = mac.nonce.hex()
  return tag

#HMAC-SHA-256 MAC:
def hmac_SHA256(s,p):
  hmac_input = p
  if isinstance(p, str):
    hmac_input = hmac_input.encode()
  mac = hmac.new(s.encode(),msg=hmac_input, digestmod=SHA256)
  return mac.digest()

#AES-CMAC:
def cmac_AES(s,p):
  cobj = CMAC.new(s, ciphermod=AES)
  cobj.update(p) #need bytes for both inputs
  return cobj.hexdigest()

def EaM(k1,k2,p):
  #Encrypt and MAC:
  Ka2B = int_to_Bytes(k2,32) #need 32-byte key
  plain_Bytes = p.encode()
  tagged = poly1305(Ka2B,plain_Bytes)
  plain_Ints = bytes_to_Int(plain_Bytes) #need int inputs 
  ciphered = simon128_Cipher(k1,plain_Ints)
  return tagged, ciphered

def MtE(k,s,iv,p):
  #MAC then Encrypt:
  tagged = hmac_SHA256(s, p)
  combined_Input = p.encode() + tagged
  print("This is adding of plaintext and tag:",combined_Input)
  iv_Int = bytes_to_Int(iv)
  print("This is the int iv:",iv_Int)
  plain_Ints = bytes_to_Int(combined_Input)
  ciphered = speck128_Cipher(k, iv_Int, plain_Ints)
  return ciphered

#first computing the authentication tag T = MAC(K2, P). Next, it creates the ciphertext by encrypting the plaintext and tag together, according to C = E(K1, P || T). 

def EtM(k,s,p):
  #Encrypt then MAC:
  plain_Bytes = p.encode()
  plain_Ints = bytes_to_Int(plain_Bytes)
  ciphered = simon128_256_Cipher(k, plain_Ints)
  ciphered_Ints = int_to_Bytes(ciphered, 16)
  secret_Bytes = s.encode()
  tagged = cmac_AES(secret_Bytes, ciphered_Ints) #need Bytes
  return tagged, ciphered

# C = E(K1, P) and a tag based on the ciphertext, T = MAC(K2, C). The receiver computes the tag using MAC(K2, C) and verifies that it equals the T received

def main():
  #Encrypt and MAC:
  print("Encrypt and MAC!:")
  Ka1 = random.getrandbits(128)
  Ka2 = random.getrandbits(128)
  plaintext1 = make_Message(16)
  tagged, cipher_A = EaM(Ka1,Ka2,plaintext1)
  print("This is tag A:",tagged)
  print("This is cipher A:",cipher_A)

  #MAC then Encrypt:
  print("MAC then Encrypt!:")
  Kb = random.getrandbits(128)
  plaintext2 = make_Message(16)
  iv = os.urandom(16)
  print("This is the iv:", iv)
  secret = make_Message(16)
  cipher_B = MtE(Kb,secret,iv,plaintext2)
  print("This is cipher B:",cipher_B)

  #Encrypt then MAC:
  print("Encrypt then MAC!:")
  Kc = random.getrandbits(256)
  plaintext3 = make_Message(16)
  secret = make_Message(16) #16 Bytes
  tagged, cipher_C = EtM(Kc, secret, plaintext3)
  print("This is tag C:", tagged)
  print("This is cipher C:", cipher_C)
main()
