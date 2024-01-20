def convert(a,b):
    c={}
    for i in range(0,len(a)):
        c[a[i]]=b[i]
    return c
print (convert([5,6,7,8],[1,2,3,4]))