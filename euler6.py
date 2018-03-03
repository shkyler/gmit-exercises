# Patrick Moore 2018-03-03
# Projec Euler Problem 6 (https://projecteuler.net/problem=6)

sumofsquares = 0
sum = 0
squareofsum = 0
counter = 1
while counter != 101:
  sumofsquares,sum,squareofsum = sumofsquares + counter**2,sum + counter,sum**2
  counter = counter + 1
print("The differnece between the sum of the squares and the square of the sums of the first 100 natural number is: ", str((squareofsum - sumofsquares)))