##This program is to test conditional statements


##Use Case 4: Check complex statments

if ((5%2 == 1) & ((4/2)==2)) | ((type("a") == type(1)) | ([1,2,3] == [3,2,1])):
   print "My expressiom is True"
else:
   print "Oh My expression is False"
   






##Logical Operators:
##   lhs $ rhs: False if any one of operands is False
##               True if both are True
##   lhs | rhs: True if any one of operands is True
##               False if both are False

##Use Case 3: Check whether two variables (a is greater than b) and (c is less than d)
##a = 3
##b = 4
##c = 5
##d = 1
##f = 8
##
##if (a > d) | (f < c):
##   print "Hurray, i am executing"
##   print "(a is greater than d) or (f is less than c)"
##else:
##    print "Hey, i have defeated If"
##    print "(a is NOT greater than d) or (f is NOT less than c)"
##    
##print "After If block"
























##Use Case 2: Check whether two variables (a & b) are of same value
##a = 3
##b = 3.0
##
##if (a == b):
##   print "Hurray, i am executing"
##   print "Values of a & b are equal"
##else:
##    print "Hey, i have defeated If"
##    print "Vales of a & b are not equal"
##    
##print "After If block"


##Use Case 1: Check whether two variables (a & b) are of same data type
##a = 3
##b = 3.0
##
##if (type(a) == type(b)):
##   print "Hurray, i am executing"
##   print "Types of a & b are equal"
##else:
##    print "Hey, i hav edefeated If"
##    print "Types of a & b are not equal"
##    
##print "After If block"
