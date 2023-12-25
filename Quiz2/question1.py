'''
Write a class called lists. The class must have a constructor with the parameter as a list and it prints it on the screen. The class has a method that counts the sum of the numbers in this list and the minimum and maximum values of it. Create a class object and pass it some list. The sum of the elements of this list, the minimum and maximum number must be printed to the screen.
'''
class lists:
    def __init__(self, list):
        self.list = list
        print(self.list)

    def sum(self):
        print("Sum:" +'\t'+ str(sum(self.list)))

    def min(self):
        print("Min:"+ '\t' + str(min(self.list)))

    def max(self):
        print("Max:" + '\t'+ str(max(self.list)))

#   Take input the values in list
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input("Enter a element:"))
    list.append(ele)
print(list)
obj = lists(list)
obj.sum()
obj.min()
obj.max()
