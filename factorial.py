# Patrick Moore 2018 -3-10
# An algorithm to calculate the factorial of an input using a function

def factorial(x):
  factcalc = 1
  counter = x
  while counter != 0:
    factcalc = factcalc * counter
    counter = counter - 1
  return factcalc

testvalues = [5,7,10]
for i in testvalues:
  print(f'The factorial of {i} is: {factorial(i)}')

