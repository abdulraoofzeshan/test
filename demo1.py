import sys
listofmarks = sys.argv
newlist = sys.argv[0]
if len(listofmarks)>0:
    for marks in listofmarks:
        newlist.append(marks+marks/10)
    print newlist
else:
    print "no marks"
