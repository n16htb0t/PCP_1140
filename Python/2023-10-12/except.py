a=[5,6,7,8]
b=[5,2,0,4]
c=[]

for i in range(0,len(a)):
    try:
        c.append(int(a[i]/b[i]))
    except:
        c.append("error")
print (c)