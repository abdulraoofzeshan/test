#Basic program to illustrate how functions work
#Uses: Reusability - using same piece of code at different places
#Readablity: It provides us more readablity

#Compute fibonacci series until 10 elements
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144



#Assign 1 to some variable <previous>
#Iterate over range(1, 11) and add current iteration's element to <previous>


##def printValues(someValue):
##    print "Current Value: " + str(someValue)
##
##printValues(12)
##printValues("Trove")
##printValues([1,2,3,4,"edfdf"])
##printValues({"key1":1, "key2":2})

##def computeFibonacci():
##    previous = 0
##    fibonacciList = []
##    for element in range(1, 10):
##        currentElement = element + previous
##        previous = element
##        fibonacciList.append(currentElement)
##    return fibonacciList
##
##listOfFirst10FibSeries = computeFibonacci(11)
##print listOfFirst10FibSeries
##
##listOfFirst25FibSeries = computeFibonacci(26)
##print listOfFirst25FibSeries

def addTwoToList(lowerLimit, upperLimit):
    previous = 2
    newList = []
    for element in range(lowerLimit, upperLimit):
        currentElement = element + previous
        newList.append(currentElement)
    print newList

lowerLimit = 30
upperLimit = 40
addTwoToList(lowerLimit, upperLimit)
lowerLimit = 130
upperLimit = 140
addTwoToList(lowerLimit, upperLimit)
