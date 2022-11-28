#    student:        Md Akramul Hasan
#    student number: 160285185
#    section:        PRG550B
#    date:           november 24, 2023
#    program:        mahasan3_PRG550X.223.TT1.py


import math
import random
import string
import collections
import datetime
import re
import time
import copy

# YOUR CODE BELOW...

def isValid(strTest) :
   # your code here...
   #check if given string is valid for password
   
   if len(strTest) < 8:
       return False
   if not strTest[0].isalpha():
         return False
   if not any(char.isupper() for char in strTest):
         return False
   if not any(char.islower() for char in strTest): 
         return False
   if not any(char in string.punctuation for char in strTest):
         return False
   return True


# end def

def fancyList( ) :
   # your code here...
   #Write a function named 'fancyList' that contains ONLY 1 line of CODE (using a list comprehension) that loops through all of the UPPERCASE letters 
   # in the alphabet and fills the list with 5 copies of each letter that is a vowel (i.e. 'A', 'E', 'I', 'O'. or 'U').

   # your code here...
   #write list comprehension loop
   #loop through all of the UPPERCASE letters in the alphabet and fills the list with 5 copies of each letter that is a vowel (i.e. 'A', 'E', 'I', 'O'. or 'U').
   #print the list
   List = [i.lower()*5 for i in string.ascii_uppercase if i in 'AEIOU']

   print(List)

   # end def

def realPattern(fn, sn, n) :
   # your code here...
   #Write a function named 'realPattern' that returns a floating point value and accepts 3 integer values: 'fn', 'sn', and 'n'
   #and displays 'n' number of terms in a sequence where the first term is 'fn',the second term is 'sn', and each subsequent term is the sum of the previous two terms.
      
   if n== 1:
      print(fn)
      return fn
   elif n==2:
      print(fn,sn)
      return sn
   else:
      print(fn,sn,end=" ")
      for i in range(2,n):
         fn, sn =sn , fn+ sn
         print(sn,end=" ")
      print()
   return sn/fn

   # returning last term divided by second last term
# end def

def nonOdds(a, b) :
   # your code here...
   #create array of all integers between a and b
   #loop through array
   #if the integer is odd, remove it from the array
   #return the array

   new_list =[] # A list which holds the numbers
   for a in range(a,b+1):
      for b in str(a):
         if int(b) % 2 != 0:
               break
      else:
         # only executed if the loop wasn't broken out of
         new_list.append(a)

   return new_list

# end def

def displayStrings(deck, coords) :
   # your code here...

   #split the each coords string into two integers
   #convert the two integers into a list of integers
   # use the list of integers to access the deck
   # print the card
   # return the list of cards
   return '-'.join([deck[int(i[0])][int(i[1],16)] for i in coords])
# end def

def main() :
   rv = isValid("abcdefghijklmnopqrstuvwxyz") # no special character (False)
   print(rv)
   rv = isValid("Mariner!")                   # all criteria OK (True)
   print(rv)
   rv = isValid("acdefGhij*012345")           # all criteria OK (True)
   print(rv)
   rv = isValid("Oscar!")                     # not at least 8 chars (False)
   print(rv)
   rv = isValid("0acdefGhij*012345")          # first character not alphabetic (False)
   print(rv)

   fancyList( )

   rv = realPattern(0, 1, 10)
   print(rv)
   rv = realPattern(1, 3, 15)
   print(rv)

   print(nonOdds(831, 862))
   print(nonOdds(4066, 4228))

   deck = [["2C", "3C", "4C", "5C", "6C", "7C", "8C", "9C", "XC", "JC", "QC", "KC","AC"],
	   ["2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "XD", "JD", "QD", "KD", "AD"],
	   ["2H", "3H", "4H", "5H", "6H", "7H", "8H", "9H", "XH", "JH", "QH", "KH", "AH"],
	   ["2S", "3S", "4S", "5S", "6S", "7S", "8S", "9S", "XS", "JS", "QS", "KS", "AS"]
	  ]
   coords=["33", "16", "28", "0A", "3C"]
   rv = displayStrings(deck, coords)
   print(rv)
   coords=["23", "24", "25", "26", "27"]
   rv = displayStrings(deck, coords)
   print(rv)

# end main( )

if __name__ == "__main__" :
   main( )
