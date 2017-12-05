import subprocess
import os

notepad = "notepad.exe"

calc = "calc"

retVar = subprocess.Popen([notepad], shell=True)
#print retVar.returncode

retVar1 = subprocess.Popen(calc, shell=True)
#print retVar1.returncode

vmware = "VpxClient.exe"

retVar2 = subprocess.Popen(vmware, shell=True, cwd="C:\Program Files (x86)\VMware\Infrastructure\Virtual Infrastructure Client\Launcher")
#print retVar2.returncode

os.system("tasklist > log.txt")

dicsriptor = open("log.txt", "r")

#print dir(dicsriptor)

linesOfLogFile = dicsriptor.readlines()

#print linesOfLogFile


def killPreocess(processName):
    if processName in line:
        print line
        spliLine = line.split(" ")
        for line1 in spliLine:
            if line1 == "":
                spliLine.remove(line1)
        print spliLine[1]
        os.system("taskkill /PID " + spliLine[1])


for line in linesOfLogFile:
    killPreocess("notepad.exe")
    killPreocess("calc.exe")
    killPreocess("VpxClient.exe")
