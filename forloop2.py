##import sys
##listofmarks=sys.argv
##print listofmarks
##listofmarks.pop(0)
##listofgracemarks=[]
##for marks in listofmarks:
##    marks=int(marks)
##    listofgracemarks.append(int(marks)+int(marks)/10)
##print(listofgracemarks)

##list1=['name1','name2','name3']
##list2=[2,3,4]
##lists=(list1,list2)
##dict={}
##for elements in  lists:
##    dict.update({'element':element})
##print(dict)

import sys
lists=sys.argv
print "User input command line arguments are \n" + str(lists)
lists.pop(0)
dict={}
currentKeyIndex = 0
print "\n Command line arguments after removing program name are \n" + str(lists)
for element in lists:
    if element == lists[currentKeyIndex+1]:
        print "Current Index is lasty element' value, so exiting"
    else:
        indexOfElement = lists.index(element)
        nextElement = lists[indexOfElement+1]
        dict.update({element:nextElement})
        currentKeyIndex = indexOfElement
print dict


##import sys
##lists=sys.argv
##lists.pop(0)
##dict={}
##for element in lists:
##    dict.update({'element1':element})
##print(dict)

