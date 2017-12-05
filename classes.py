##defining a classes 
class myclass:
    
    def __init__(self, l, b):
        self.length=l
        self.breadth=b
        

    def computearea(self):
        print self.length*self.breadth
       

    def computediag(self):
        print self.length+self.breadth
        


obj1=myclass(3,4)
obj1.computearea()

        
