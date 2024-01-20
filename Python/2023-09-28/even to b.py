import random
a=[]
b=[]
for i in range(0,50):
    a.append(random.randrange(0,100))
print (a)
for i in range(0,len(a)):
    if a[i]%2==0:
        b.append(a[i])
print (b)