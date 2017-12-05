class myclass:
    def __init__(self,x,y):
        self.a=x
        self.b=y
    def computeadd(self):
        print self.a+self.b
    def computemul(self):
        print self.a*self.b
obj1= myclass(3,4)
obj1.computeadd()

obj2= myclass(80,100)
obj2.computemul()

