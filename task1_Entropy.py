'''
Question 1 (answer all 4 parts)

[15 points] Develop a program that collects and combines entropy from all three of the following sources: random.org (via http), OpenSSL, /dev/urandom
[15 points] Using the entropy source from part A as a seed, write a program that generates sequences of pseudorandom bits
[10 points] Add a bias to the pseudorandom bits in part B so that 80% of the time the output is bit 0
[10 points] Remove the bias from the output of part C using a von Neumann entropy extractor so that the probability of bit 1 or bit 0 is again 50%.
'''
#NOTE: MUST INSTALL RANDORG in Repl.it first to generate source 3 numbers
import randomorg as ro #required for fetching random.org
import os
import OpenSSL #need library
import random 
import sys
import numpy as np
from scipy.stats import entropy
import os.path

#sources:
#1 urandom
def source1():
  ur = os.urandom(5)
  newUR = hash(ur)
  print("This is source 1: ", newUR)
  return newUR
source1()
sr1 = source1()

#2 OpenSSL
def source2():
  stream = os.popen('openssl rand -hex 8')
  rand_bytes = stream.read()
  newRAND = hash(rand_bytes)
  print("This is source 2: ", newRAND)
  return newRAND
source2()
sr2 = source2()

#3 random.org
# Generate integers between 1 and 100
def source3():
  num = ro.integers(20, minimum=1, maximum=100, base=10)
  NUM = bytes(num)
  newNUM = hash(NUM)
  print("This is source 3: ", newNUM)
  return newNUM
source3()
sr3 = source3()
  #need to make an int?

def entro():
  #combines entropy from all three sources
  final = hash(sr1+sr2+sr3)
  print("This is the combined entropy: ", final)
  return final
entro()
result = entro()
  
#generate sequence of pseudorandom bits
def makeRand(result):
  SEED = random.seed(a=int(result), version=2)
  pseudo = random.getrandbits(10)
  print("This is the pseudo numbers: ", pseudo)
  return pseudo
#makeRand(result)
RESULT = makeRand(result)

#Add a bias to the pseudorandom bits in part B so 
#that 80% of the time the output is bit 0

def bias():
  see = random.randrange(0, 100, 1)
   #less than or equal to 80
  if see <= 80:
    return 0
   #greater than 80 is a 1
  else:
    return 1
  #print(see)
bias()

def cookie():
  size = 100
  a = []
  for x in range(size):
    a.append(bias())
    a.append(RESULT)
    print("This should be the biased array: ", a)
    return a
cookie()
COOKIE = cookie()
#returns biased array of numbers based on part B.

#Remove the bias from the output of part C using a von Neumann entropy extractor so that the probability of bit 1 or bit 0 is again 50%.
def removeBias(COOKIE):
  last = COOKIE[0]
  size = len(COOKIE)
  #print(COOKIE[0])
  for i in range(size-1):
    current = COOKIE[i+1]
    if current == 1 and last == 0: 
      return 1
    elif current == 0 and last == 1:
      return 0
    last = current
    return COOKIE
removeBias(COOKIE)
REMOVE = removeBias(COOKIE)
#should return unbiased array of numbers
#making new array to do so
def brownie():
  size = 50
  b = []
  for y in range(size):
    b.append(REMOVE) #algorithm for unbiased
    print("This should be the unbiased array: ", b)
    return b
brownie()
