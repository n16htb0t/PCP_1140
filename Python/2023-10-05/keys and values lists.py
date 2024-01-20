import random
a={}
keys=[]
values=[]
for i in range(0,10):
    a[random.randrange(0,100)]=random.randrange(0,100)
print (a)
for i in a.keys():
    keys.append(i)
for i in a.values():
    values.append(i)
print (keys,values)