##Increase the salaries of employees by double
##Algorithm
##1. Define a list of salary numbers with integer data types
##    Check if list is empty
##    Check if each element is a integer
##    Check if each evalue is non-negative
##    Check whether the element has only numeric data
##2. Loop over the each element of the defined list and
##3. Multiply each element by 2 and print
##4. Store each element in new list

##import sys
##
##print "User given list of salaries" + str(sys.argv)
##
##newList = []
##
##sys.argv.pop(0)
##
##for salary in sys.argv:
##    
##    newList.append(int(salary) * 2)
##
##print newList







import sys
print "user given list of salaries"+str(sys.argv)
newlist=[]
sys.argv.pop(0)
for salary in  sys.argv:
    newlist.append(int(salary)*2)
print(newlist)





##Prepare a dictionary From two lists of equal length
##(With one having keys another having values)
##listOfKeys = ["a", "b", "c"]
##listofvalues = [1, 2, 3]

##newDict = {}

#Mtethod 1
##newDict.update({listOfKeys[0]:listofvalues[0],
##                listOfKeys[1]:listofvalues[1],
##                listOfKeys[2]:listofvalues[2]})

#Mtethod 2

##index = 0
##for key in listOfKeys:
##    newDict.update({key: listofvalues[index]})
##    index = index + 1
##    
##print newDict






##[] = square brackets
##{} = Flower Bracket/ Curly
##() = paranthesis
