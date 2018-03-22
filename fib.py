# Patrick Moore
# A program that displays Fibonacci numbers using people's names.
# Note this code was copied from Ian McLoughlin and modified (https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py)

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

name = "Moore"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno

ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)

# In Week 1 I made the following comments on the discussion board:
# My name is Patrick, so the first and last letter of my name (P + K = 16 + 11) give the number  27. The 27th Fibonacci number is 196,418.

# In Week 2 I made the following comments on the discussion boards:
# I copied the code from the GitHub webpage, changed the surname to “Moore” and ran it in Visual Studio Code.
# The result was as follows:
# My surname is Moore 
# The first letter M is number 77
# The last letter e is number 101
# Fibonacci number 178 is 7084593923980518516849609894969925639

# Before running the code I had a look at the ord() function to see if I could determine what it did.
# I could tell that it converted a character to a number but I wasn’t sure what number it was. My first guess was that it converted it to the alphabetical order of the character (like we did manually last week). However, once I ran the program I could tell that was not the case!
# A quick google search later and I learned that the ord() function in Python returns the unicode code for that character. I also learned that there is a reciprocal function chr() that will return the character for a given unicode reference. 
# To test this, I ran the following code:

# print(chr(77))

# the program returned “M” (without quotation marks!)
