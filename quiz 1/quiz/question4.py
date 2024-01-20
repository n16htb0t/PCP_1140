#You have two lists: [5,6,1,2] and [1,2,3,4]. The program must calculate the sum of these lists, elements by element. The final output must be: [6,8,4,6]
a=[5,6,1,2]
b=[1,2,3,4]
sum=[]
for i in range(len(a)):
    sum.append(a[i]+b[i])
print(sum)