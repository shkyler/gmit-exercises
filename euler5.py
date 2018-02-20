# Patrick Moore 2018-02-18
# Project Euler Problem 5 - https://projecteuler.net/problem=5
check = 0
x = 2520
while check != 1:
    
    if x % 11 == 0 and x % 12 == 0 and x % 13 == 0 and x % 14 == 0 and x % 15 == 0 and x % 16 == 0 and x % 17 == 0 and x % 18 == 0 and x % 19 == 0 and x % 20 == 0:
        check = 1
        print (x)
    else:
        x = x + 2520
        
    