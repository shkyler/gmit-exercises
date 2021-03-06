 ![GMIT Logo](/img/GMITLOGO.jpg)
# GMIT Programming and Scripting Exercises                                                                                                        
This respository is a place to share my GMIT exercises for the Programming and Scripting module
## Compilation
All the files in this repository are written in the [Python](https://www.python.org/) [1]programming language.
## Weeks 1 and 2
fib.py contains my answers to the exercise for week 2. The script is based on an algorithm to calculate numbers in the [fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_number) [2]
Note that at the bottom of the script I have added my comments from the discussion forum (week 1 and week 2) as comments in the code.
## Week 3
collatz.py contains my answer to the exercise for week 3. Details of the collatz conjecture can be found [here](https://en.wikipedia.org/wiki/Collatz_conjecture) [3].
Note that I initially did it with "n = 17" hard coded into the program, then I changed it to ask the user for an integer so it can be used for the general case.
Also I noticed that integer division resulted in floating point numbers - the printout looked a little strange to me so I rounded all the outputs using the built-in Python [round function](https://docs.python.org/3/library/functions.html#round) [4] (so that there are no decimels).
## Week 5
euler5.py contains my solution to [project euler problem 5](https://projecteuler.net/problem=5)[5].
Note I intitially completed this in week 4 using a while loop and an if statement, I then reworked it in week 5 to include a for loop and a range statement as requested my Ian McLoughlin. The comments in the code should explain my algorithm.
## Week 6
openfile.py contains my solution to problem asking us to open the [iris.csv](https://en.wikipedia.org/wiki/Iris_flower_data_set) [6] file and then print out the values in a nice format. First, I [downloaded the csv file](http://archive.ics.uci.edu/ml/datasets/Iris) [7] and saved in a data folder as Ian did in the video lecture. I then wrote the code to open the file and go though it line by line printing out the values to 1 place of decimel with 1 space between the columns. There are some comments in the code. I used the [Python Tutorial](https://docs.python.org/3/tutorial/) [8] as a reference for this one to determine how to format floating point numbers. There was some trial and error but I got there!
## Week 7
factorial.py contains my solution to the problem asking us to create a function to calculate the [factorial](https://en.wikipedia.org/wiki/Factorial) [9] of a given input. We then had to test the fuction with the values 5,7 and 10. I have included comments in the code to explain the algorithm and I used a for loop to do the testing.
## References
1. [1] Python Software Foundation. Welcome to Python (_https://www.python.org_)
2. [2] Wikipedia. Fibonacci Number (_https://en.wikipedia.org/wiki/Fibonacci_number_)
3. [3] Wikipedia. Collatz Conjecture (_https://en.wikipedia.org/wiki/Collatz_conjecture_)
4. [4] Python Software Foundation. Documentation.  (_https://docs.python.org/3/library/functions.html#round_)
5. [5] Project Euler. Problem 5 (_https://projecteuler.net/problem=5_)
6. [6] Wikipedia. Iris Flower Data Set (_https://en.wikipedia.org/wiki/Iris_flower_data_set_)
7. [7] UC Irvine Machine Learning Repository. Iris data set.(_http://archive.ics.uci.edu/ml/datasets/Iris_)
8. [8] Python Software Foundation. The Python Tutorial (_https://docs.python.org/3/tutorial/_)
9. [9] Wikipedia. Factorial. (_https://en.wikipedia.org/wiki/Factorial_)

