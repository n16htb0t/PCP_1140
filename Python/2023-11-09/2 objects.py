class Figure():
    
    def __init__(self,tipi):
        self.tipi=tipi
        print ("I am "+self.tipi)
    def square(self,side1,side2):
        self.side1=side1
        self.side2=side2
        return self.side1*self.side2   
a=Figure("Mr. Square")
print (a.square(5,6))
b=Figure("Mrs. Rectangle")
print (a.square(6,8))