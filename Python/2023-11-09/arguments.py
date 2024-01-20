class Figure():
    tipi="Rectangle"
    def __init__(self,side1,side2):
        self.side1=side1
        self.side2=side2
        print (side1,side2,"hello")
    def square(self):
        return self.side1*self.side2   
a=Figure(5,6)

print (a.square())