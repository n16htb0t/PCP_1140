a,b,c=[],[],[]
for i in range(0,5):
    a.append(int(input("insert the number")))
print (a)
for i in range(0,len(a)):
    if a[i]%2==0:
        b.append(a[i])
    else:
        c.append(a[i])
print (b,c)