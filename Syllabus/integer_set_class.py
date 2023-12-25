class intSet():
    def __init__(self):
        self.vals = []
    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
        return e in self.vals
    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
    def __str__(self):
        self.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}'

intSet = intSet()
intSet.insert(3)
intSet.insert(4)
intSet.insert(5)
intSet.insert(6)

print(intSet)
print(intSet.member(3))
print(intSet.member(7))
intSet.remove(3)
print(intSet)
# Output:
# {3,4,5,6}
# True
# False
# {4,5,6}
