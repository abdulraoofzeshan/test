##listofmarks=[]
##newlistmarks=[]
##
##if len(listofmarks)>0:
##    for marks in listofmarks :
##        
##        newlistmarks.append(marks+marks/10)
##    print newlistmarks
##else:
##    print "No marks list. please enter the

#Input variables studentmarkslist.py name1 20 name2 25 name3 23
import sys
lists=sys.argv
#print "User input command line arguments are \n" + str(lists)
lists.pop(0)
dict={}
currentKeyIndex = 0
#print "\n Command line arguments after removing program name are \n" + str(lists)
for element in lists:
    if element == lists[currentKeyIndex+1]:
        print "Current Index is lasty element' value, so exiting"
    else:
        indexOfElement = lists.index(element)
        nextElement = lists[indexOfElement+1]
        dict.update({element:nextElement})
        currentKeyIndex = indexOfElement
    
print dict
