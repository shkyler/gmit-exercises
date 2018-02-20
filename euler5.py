# Patrick Moore 2018-02-18
# Project Euler Problem 5 - https://projecteuler.net/problem=5
# Note: I had initially completed this during week 4 using a while loop and an if statement
# I did it again this week with the for loop and range statement

check = 0                           # check is used as a boolean to stop the while loop later
x = 2520                            # in the problem statement 2520 is the the lowest number divisible by number 1 - 20 we can use this as a starting point
modsum = 0                          # this will be used later to sum up the modulii
numrange = range(11,21)             # as x is starting at 2520, all muliples of this number will be checked in the range 11 to 20

def modcheck():                     # this function will be used to check if each number between 11 and 20 is a divisor for a given value of x
    global x,modsum                 # this statement allows the use of global variables in the function
    for i in numrange:              
        modsum = modsum + (x % i)   # the remainders of division are added to "modsum"

while check != 1:
    modcheck()                      # in the while loop the modcheck() function is called   
    if modsum == 0:                 # if all numbers are evenly divisible then modsum will be zero    
        check = 1                   # this ends the while loop   
        print ("The lowest number divisable by all numbers 1 - 20 is: ", x)
    else:
        x = x + 2520                # otherwise we move on to the next multiple of 2520 and check that
        modsum = 0                  # modsum needs to be reset to zero before the next iteration 
        
    