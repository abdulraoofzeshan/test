import sys
list=sys.argv
print list
list1=list.pop(0)
print list1
sum = 0
for marks in list:
    marks = int(marks)
    sum = marks + sum
studentpercentage = (sum/6)
print studentpercentage
if studentpercentage <=35:
    print 'fail'

if studentpercentage >=35:
    print 'thirdclass'

if studentpercentage >=50:
    print 'secondclass'

if studentpercentage >=60:
    print 'firstclass'

if studentpercentage >=75:
    print 'dinctintion'

   

       
       
    
    
    
