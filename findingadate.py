import sys
print sys.argv
inputlist=sys.argv
year=inputlist[1]
year=int(year)

if year % 4 == 0:
        print """Year is divisible by 4, there is a
        possibility of it being a leap year"""
        if year % 100 == 0:
            if year % 400 == 0:
                print "It is a leap year"
            else:
                leap = False
                print "Year is not leap year"
        else:
            print "Year is a leap year"

else:
        leap = False
        print "Year is not divisible by 4, so cannot by leap year"
    
dictOfMonths = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
if dictOfMonths==1


