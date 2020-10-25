# Patrick Moore 2018-02-05
# The Collatz Conjecture - https://en.wikipedia.org/wiki/Collatz_conjecture
# This is now on github

n = int(input("Please enter an integer: ")) # I revised the code to request an integer from the user

print(n)                                # The script will print the initial number first 
                       
while n != 1:                            # The script will run until the number reaches "1"
    if n % 2 == 0:                       # For even numbers divide by 2 and print before looping again
        n = n/2                          # For odd numbers multiply by 3 and add 1 before looping again
        print(round(n))                  # in Python3, integer division results in a float
    else:                                # I rounded the floats so they look neater in the print out using the built in round function
        n = ((3 * n) + 1)
        print(round(n))
print("End")