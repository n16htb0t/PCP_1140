import random
a=[]
for i in range(0,10):
    a.append(random.randrange(0,100))
print (a)
b=open("hi.txt","w")
b.write(str(a))
b.close()
