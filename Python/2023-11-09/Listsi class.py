class Listi():
    def __init__(self, a):
        self.a=a
        print (self.a)
    def average(self):
        return sum(self.a)/len(self.a)
        
new=Listi([5,6,7,2])
print (new.average())
