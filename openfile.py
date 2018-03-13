# Patrick Moore 2018-02-27
# Iris Data Set - (http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data)
# Reference for the problem - (https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) fromt the Python Tutorial

with open("data/iris.csv", "r") as myfile:                         # this statement opens the file (iris.csv) and assigns it as "myfile"
  for line in myfile:                                              # the for loop goes through each line in the file line by line 
    rows = line.split(',')[0:4]                                    # rows is a new string that temporarily stores the data values from each of the first 4 columns of every line
    print("{:.1f} {:.1f} {:.1f} {:.1f}".format(float(rows[0]),float(rows[1]),float(rows[2]),float(rows[3]))) #finally the program prints out each line formatted to 1 place of decimel with a space between each column
                                                                                                             #the values in "rows" are stored as strings so need to be converted to floats in order to use the "f" formatting command 