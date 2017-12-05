pathOfafile= "E:\\PythonPrograms\\complicatedFile.txt"
##print pathOfafile
filepe= open(pathOfafile,"r")
lines=filepe.readlines()
##print lines
for line in lines:
    line=line.strip("\n ")
    splitlines=line.split("  ")
print splitlines
    
