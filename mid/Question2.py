import random
a= [random.randint(0,100) for i in range(100)]
while 5 in a:
    a.remove(5)
print(a)
