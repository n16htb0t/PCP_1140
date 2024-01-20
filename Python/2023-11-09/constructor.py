class Figure():
    tipi="Rectangle"
    side1=5
    side2=6
    def __init__(self):
        print ("hello")
    def square(self):
        return self.side1*self.side2
          
a=Figure()
print (a.tipi,a.side1)
print (a.square())