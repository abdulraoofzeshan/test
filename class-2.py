##write a program to find a percentages of a students while performing a class
class student:
    
    def __init__(self,name,sno,maths,science,social):
        
        self.sname=name
        self.ssno=sno
        self.smaths=maths
        self.sscience=science
        self.ssocial=social
        
    def computepercentage(self):
        sum=self.smaths+self.sscience+self.ssocial
        percentage=sum/3
        return percentage
raufs=student("abdurraoof",1,60,70,80)
percentage=raufs.computepercentage()
print raufs.sname
print raufs.ssno
print percentage

