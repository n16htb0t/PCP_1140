class coordinate():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def show(self):
        return (self.x,self.y)
    def distance(self,other):
        x_diff_sq = (self.x-other.x)**2
        y_diff_sq = (self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
    def __str__(self):
        return str(self.x)+","+str(self.y)
    
    def __add__(self,other):
        return str(self.x+other.x)+","+str(self.y+other.y)
    
a=coordinate(3,4)
b=coordinate(5,6)
print(a.x)
print(b.y)
print(a.show())
print(b.show())

print(a.distance(b))
print(b.distance(a))
print(coordinate.distance(a,b))
print(a)
print(b)
print(a+b)