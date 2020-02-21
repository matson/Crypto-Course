#2. Implement a program that calculates the frequency each letter appears in a given string and demonstrate its correctness using the first 10 paragraphs of Lorem Ipsum from

#1). Define random string and function
#2). Use counter() in python 3...
from collections import Counter

#Used Python 3 built-in counter function
#Function calculates frequency of letters in any string or paragraph
#Input your string:
string = input("place string here!")

def sequenceLetters(string):

  sequence = Counter(string)
  print(str(sequence))
  return(str(sequence))

sequenceLetters(string)


