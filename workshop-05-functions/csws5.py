
def printNTimes(whatToPrint, howManyTimesToPrint):
    for i in range(0, howManyTimesToPrint, 1):
        print(whatToPrint)
        howManyTimesToPrint = 10

printNTimes("yo it's friday")
print(howManyTimesToPrint)

#### Part 2

def findSum(aListToSum):
    numSum = 0
    for x in aListToSum:
        numSum += x

    return(numSum)


ethanGrades = [4, 4, 4]
result = findSum(ethanGrades)
print(result)