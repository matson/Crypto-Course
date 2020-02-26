#uses python library
#write function which takes a number range and print out a permutation of that range
from itertools import permutations 

def permutation(first, last):
  p = list(permutations(range(first, last)))
  print(p)
  return p

permutation(1,5)
