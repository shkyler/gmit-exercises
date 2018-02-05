# Patrick Moore 2018-02-05
# The Collatz Conjecture - https://en.wikipedia.org/wiki/Collatz_conjecture

n = int(input("Please enter an integer: ")) # I revised the code to request an integer from the user

print(n)             
                       
while n != 1:
    if n % 2 == 0:
        n = n/2
        print(round(n)) #in Python3, integer division results in a float
    else:               # I rounded the floats so they look neater in the print out
        n = ((3 * n) + 1)
        print(round(n))
