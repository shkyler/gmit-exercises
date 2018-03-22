# Patrick Moore 2018 -3-10
# An algorithm to calculate the factorial of an input using a function
# Definition of the factorial from wikipedia - (https://en.wikipedia.org/wiki/Factorial)
# The function is to be tested by calculating the factorial of 5, 7 and 10

def factorial(x):                                    # define a function called factorial
  factcalc = 1                                       # variable to hold the result of the calculations as we pass through the loop - value set to 1 as this will not alter any multiplcation calculations
  counter = x                                        # using a local varialble for a counter otherwise the fuction will change the value of x - this may not be desirable if x is a global variable used elsewhere in a script 
  while counter != 0:                                # using a while loop to pass through all the values between the input and 1
    factcalc = factcalc * counter                    # on each pass through the loop multiply the factcalc variable by the counter 
    counter = counter - 1                            # decrease the value of the counter by 1 before passing through the loop
  return factcalc                                    # the function returns the final value of fact calc

testvalues = [5,7,10]                                # to test the function I created a list with the test values in it
for i in testvalues:                                 # a for loop is used to pass through the test values and print the factorial for each number
  print(f'The factorial of {i} is: {factorial(i)}')

