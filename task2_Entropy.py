import random

"""
[5 points] Write a function that gets four bits as input and returns the addition modulo 2 of all these bits
[10 points] Write a program that processes an input array of 16 bits as follows: 
(1) using the function of part A, 
compute the addition modulo 2 of bits at index 11, 13, 14 and 16 of the input array (note, indexing starts at position and store the result in the first index of the output array, 
(2) store thehh first 15 bits of the input array into indexes 2-16 
of the output array, 
(3) return the output array
[10 points] Create a pseudorandom number generator using the program of part B as follows: 
(1) use a 16-bit random seed as the input array, 
(2) the output array become the next input array, 
(3) repeat the previous steps to generate many pseudorandom numbers.
[25 points] Is the PRNG of part C a secure PRNG? If it is secure, explain why it achieves backtracking resistance 
and prediction resistance. It is not secure, write a program that generates the 5 next and 5 previous numbers of a given 16-bit value.

"""

#1
#takes four bits and returns the addition modulo 2 of all these bits
def four(a,b,c,d):
  combo = (a+b+c+d) % 2
  print("Addition 4 Mod combo: " , combo)
  return combo

#2
arr = [1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,1] #example
def sixteen(arr):
  #indexes
  arr11 = arr[10]
  arr13 = arr[12]
  arr14 = arr[13]
  arr16 = arr[15]
  compute = four(arr11,arr13,arr14,arr16) #use def four.
  output = bytearray(16)
  output[0] = compute
  #print(output)
  #store 15 bits of input array into indexes 2-16
  for i in range(1, 15):
    output[i] = arr[i-1]
    i += 1
    
  print("Solution for problem 2: ", output)
  return output
sixteen(arr)

#3
#16-bit random seed as input array
randomarray = bytearray(16)
randomarray[0] = 1
randomarray[1] = 0
randomarray[2] = 1
randomarray[3] = 0
randomarray[4] = 1
randomarray[5] = 0
randomarray[6] = 1
randomarray[7] = 1
randomarray[8] = 1
randomarray[9] = 0
randomarray[10] = 1
randomarray[11] = 1
randomarray[12] = 0
randomarray[13] = 0
randomarray[14] = 1
randomarray[15] = 0
def pseudo(r):
  output1 = sixteen(r)
  output2 = sixteen(output1)
  output3 = sixteen(output2)
  output4 = sixteen(output3)
  output5 = sixteen(output4)
  print("this is output 1:", output1, "this is output 2 :", output2, "this is output 3 :", output3, "this is output 4 :" , output4, "this is output 5 :", output5)
  #output PRNG
pseudo(randomarray)

#4
"""
According to the resultant outputs, the PRNG IS NOT SECURE since it does not guarantee backtracking resistance and prediction resistance.  They (bits) can be possible to recover and future bits can also be predicted.  According to the textbook, the PRNG should call refresh regulary with R values that are completely unknown to an attacker.
write a program that generates the 5 next and 5 previous numbers of a given 16-bit value.
This insecure situation is like the LFSR. If a specific bit length, an attacker needs only n output bits to recover the LFSR’s initial state, allowing them to determine all previous bits and predict all future bits.
Goal: implementation of Berklekamp Massey algorithm
"""
randomarray2 = bytearray(16)
randomarray2[0] = 1
randomarray2[1] = 0
randomarray2[2] = 1
randomarray2[3] = 0
randomarray2[4] = 1
randomarray2[5] = 0
randomarray2[6] = 1
randomarray2[7] = 1
randomarray2[8] = 1
randomarray2[9] = 0
randomarray2[10] = 1
randomarray2[11] = 1
randomarray2[12] = 0
randomarray2[13] = 0
randomarray2[14] = 1
randomarray2[15] = 0

def securePseudo(r):
  output1 = sixteen(r)
  output2 = sixteen(output1)
  output3 = sixteen(output2)
  output4 = sixteen(output3)
  output5 = sixteen(output4)
  print("The next five ouputs : ", output1, output2, output3, output4, output5)
  #only n output bits to recover the LFSR’s initial state:
securePseudo(randomarray2) 

#pseudo code for last part 
def securePseudo2(o1,o2,o3,o4,o5):
  #previous = reverse shifting of above function
  #return previous
  #securePseudo(output)
  return 0


