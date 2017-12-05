

#All about class

#Defining a class
class myClass:

    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    
    def computeArea(self):
        print self.length * self.breadth

    def computeDiag(self):
        print self.length * self.length + self.breadth * self.breadth


#Instantiating the class -> an object
obj1 = myClass(3,4)
obj1.computeArea()



obj2 = myClass(5, 7) 
obj2.computeArea()
