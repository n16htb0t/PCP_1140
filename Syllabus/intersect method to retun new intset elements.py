#s1.intersect(s2) returns a new intSet containing elements that appear in both sets s1 and s2 having no common elements
# add a appropriate method so that len(s) returns the number of elements in s

class intSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def intersect(self, other):
        commonValueSet = intSet()
        for val in self.vals:
            if other.member(val):
                commonValueSet.insert(val)
        return commonValueSet

    def __len__(self):
        return len(self.vals)

    def __str__(self):
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
s1 = intSet()
s1.insert(1)
s1.insert(2)
s1.insert(3)
s1.insert(4)
s1.insert(5)
s1.insert(6)
print(s1)
print(len(s1))
