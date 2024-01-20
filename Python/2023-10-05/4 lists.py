import random
a,odd_keys,odd_values,even_keys,even_values={},[],[],[],[]
for i in range(0,10):
    a[random.randrange(0,100)]=random.randrange(0,100)
print (a)
for i in a.keys():
    if i%2==0:
        even_keys.append(i)
    else:
        odd_keys.append(i)
    
for i in a.values():
    if i%2==0:
        even_values.append(i)
    else:
        odd_values.append(i)
print (odd_keys,odd_values,even_keys,even_values)