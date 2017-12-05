import subprocess
import os
notepad='notepad.exe'
calc='calc.exe'
matlab='matlab.exe'
##retvar=subprocess.Popen([notepad], shell=True)
##print os.system(notepad)
##retvar1=subprocess.Popen([matlab],shell=True ,cwd='C:\Users\raoof')
os.system('tasklist>log.txt')
discriptor = open('log.txt','r')
print ('discriptor')
print dir(discriptor)
logoflines=discriptor.readlines()
print logoflines

def killprocesses(processname):
 if processname in lines:
    print line
    splitline=line.split("")
for line1 in splitline:
 if line1=="":
     splitline.remove("")
     print splitline[1]
     os.system("taskkill/PID" +splitline)

for line in logoflines:
        killprocesses("notepad.exe")
        killprocesses("calc.exe")
        killprocesses("matlab.exe")
                      

                
