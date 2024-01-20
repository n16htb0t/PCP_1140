#3.	You have an empty list; fill it with 20 random elements. All even elements place to the different list, all add elements to the different list. You must use for twice.
import random
a=[]
even=[]
odd=[]

for i in range(20):
    a.append(random.randint(1,100))
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])

print(even)
print(odd)