# Because the dummy data is stored as a CSV file, there is a Python library called "csv"
# that has some prepared functions to read and write csv files. Because we won't be using
# Python later on for reading in CSV files, I'm prewriting this code first to save you time
# on the more important concepts behind data structure manipulation, functions, and for/while loops.

# this command imports in the csv package
# (which is included in the python installation by default,
# but is not loaded hence why we need to load it ourselves)
import csv

# the below code reads in the csv file and appends each row to myData
# if you print myData, you'll see that it is a list of lists (where each 
# sublist is a row in the original data)
myData = []
with open("/Users/ethanburns/Documents/CS_Workshop/dummyData.csv", "r") as csvfile:
  csvReader = csv.reader(csvfile, delimiter = ",")
  for row in csvReader:
    myData.append(row)
    
print(myData)

# Here I've included a custom function that you might find useful.
# This function takes in a value and checks if it can be converted into
# type float. If it can be, the function returns True. If the value cannot be converted
# to float, the function returns False.
def isFloat(value):
  try:
    float(value)
    return(True)
  except ValueError:
    return(False)


####################
# TODO - Question #1
####################
# Create a dictionary where each key is the column nane (i.e. "sample" or "CD3")
# and the corresponding value is a list of values in that specific column. If the column
# contains a number, I want you to cast (i.e. convert) that value into a float type before you add
# it into the dictionary.

# Hint: if you run into a TypeError at some point...print out myData and see what values
# are stored there.

# // Write your code here //
myDataDict = {}

for k in range(0,len(myData[0])):

    named = myData[0][k]
    myDataDict[named] = []
    
    for i in range(1, len(myData)):
        
        val = myData[i][k]
        if isFloat(val) == True:
          val = float(val)
        
        myDataDict[named].append(val)

# print out your dict to make sure it's right!

print(myDataDict)

####################
# TODO - Question #2
####################
# Write a function called findMean that takes in a list of values and returns the mean.

# HINT: If you're using Python 2, you will need to watch out that you're not doing integer division.

# // Write your code here //

def findMean(dat):
    sum = 0
    for i in dat:
      sum += i
    avg = sum/len(dat)
    return(avg)





# Test if your function works! Uncomment out the below lines to test.
print(findMean([3, 4, 6])) # this should return 4.3 repeating.
print(findMean([1])) # this should return 1


####################
# TODO - Question #3
####################
# Write a function called findFoldChange that takes in two arguments: listA and listB.
# Return the fold change of the mean of listB over mean of listA (i.e. listB's mean / listA's mean)

# HINT: remember that you wrote a function above that's called findMean. Use it!
# HINT: If you're using Python 2, you will need to watch out that you're not doing integer division.

# // Write your code here //

def findFoldChange(listA, listB):
   fold = findMean(listB) / findMean(listA)
   return(fold)

# Test if your function works! Uncomment out the below lines to test.
print(findFoldChange([3, 4, 5], [3, 4, 5])) # this should return 1 since 4 / 4 = 1
print(findFoldChange([5], [1])) # this should return 0.2 since 1 / 5 = 0.2
print(findFoldChange([1], [5])) # this should return 5 since 5 / 1 = 5


####################
# TODO - Question #4
####################
# With your new functions, calculate the fold change between the mean expression of all unstim and the mean expression of all stim samples for
# each column that has numeric values in it (i.e. the last 6 columns in the data table).

# Your output should be printed to the console along with the column name: "Fold change between stim/unstim for CD3 is _______"

# As a hint, the CD3 fold change comparison would be done by using your findFoldChange() function on two lists:
# listA would be the unstimmed samples would consist of [11.23, 19.21, 43.32, ...and so on] 
# listB would be the stimmed samples [79.14, 88.99, 11.52, ...and so on]

# findFoldChange(listA, listB) would give you your fold change. This question requires you to do this calculation for CD4, CD8, CD69, CD25, and CD38 as well.

# As an additional hint: feel free to create additional functions!
# You are NOT limited to just the two functions that you have created in the previous questions.


# // Write your code here //

def findIDX(dataSet, row, condition):
   
  idx = []
  for i in range(0, len(dataSet[row])):
    val = dataSet[row][i]
    if val == condition:
      idx.append(i)
  return(idx)

unstim = findIDX(myDataDict, 'treatment', 'unstim')
stim = findIDX(myDataDict, 'treatment', 'stim')


def findVals(dataSet, row, samples):
   
  vals = []
  for i in samples:
    val = dataSet[row][i]
    vals.append(val)
  return(vals)


names = ["CD3", "CD4", "CD8", "CD69", "CD25", "CD38"]
for i in names:
  unstimVals = findVals(myDataDict, i, unstim)
  stimVals = findVals(myDataDict, i , stim)
  fc = findFoldChange(unstimVals, stimVals)
  print("Fold Change between stim/unstim for", i, 'is', fc)


