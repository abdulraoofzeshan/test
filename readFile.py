#import os
#pathOfFile = os.path.join("E:\PythonPrograms", "readFile.py")
pathOfFile = "E:\\PythonPrograms\\simpleFile.txt"
#print pathOfFile
fileDe = open(pathOfFile, "r")
listOfLines = fileDe.readlines()

for line in listOfLines:
    line = line.strip("\n")
    splittedLine = line.split(" ")
    print splittedLine
