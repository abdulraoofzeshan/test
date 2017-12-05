
#Create a file with some formatted data
#Read the file into a list -> Every element of the list corresponds to the line of file
#Parse the list and find out the dates in every element of the list

fd = open("logDate.txt", "w")
fd.writelines("Once there was a nation of Goths obsessed with dates. Yes dates like 12-05-1001!\n")
fd.writelines("One might wonder from where this typical representation of dates come from?\n")
fd.writelines("Well, the Mayans have first adopted the format 13/5/0001 to denote day/month/year respectively!\n")
fd.writelines("Later, the nation of Goths have worked upon the format & bcame up with the format like 17-9-1900!\n")
fd.writelines("With that ended the date game!\n")
fd.close()

import re

discriptor=open("logDate.txt","r")
logoflines=discriptor.readlines()
print logoflines

dateDashPattern = "[0-9][0-9]+-[0-9]+-[0-9][0-9][0-9][0-9]"
dateSlashPattern = "[0-9][0-9]+/[0-9]+/[0-9][0-9][0-9][0-9]"

for line in logoflines:
    line1 = line.split(' ')
    for ele in line1:
        reObject = re.match(dateDashPattern, ele)
        
        reObject1 = re.match(dateSlashPattern, ele)
        
        if reObject != None:
            print "Mubaarak ho! Element is a date"
            print reObject.group()
            
        if reObject1 != None:
            print "Mubaarak ho! Element is a date"
            print reObject1.group()
