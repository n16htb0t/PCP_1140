def convert(a):
    b,c=[],[]
    for i,j in a.items():
        b.append(i)
        c.append(j)
    return b,c
    
print (convert({5:12,6:18,12:29,13:25}))