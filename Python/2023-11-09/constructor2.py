class Figure():
    tipi="Rectangle"
    def __init__(self):
        self.side1=5
        self.side2=6
        print ("hello")
    def square(self):
        return self.side1*self.side2    
a=Figure()
print (a.tipi,a.side1)
print (a.square())