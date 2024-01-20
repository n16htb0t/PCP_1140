import random
a = [[],[],[]]
for i in a:
    i.append(random.randint(0,15))
    i.append(random.randint(0,15))
total = sum([sum(i) for i in a])
print(a)
print(total)
