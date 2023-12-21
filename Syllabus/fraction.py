# a= fraction(1,2) #1/2
# b= fraction(2,3) #2/3
# print(a)  = 1/2
#print(a+b) = 1/2+2/3 = 7/6

class fraction():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return str(self.x)+"/"+str(self.y)
    def __add__(self,other):
        return str(self.x+other.x)+"/"+str(self.y+other.y)
    
    def __sub__(self,other):
        return str(self.x-other.x)+"/"+str(self.y-other.y)

a=fraction(3,14)
b=fraction(5,6)
print(a)
print(b)
print(a+b)
print(a-b)