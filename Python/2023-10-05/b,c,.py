a=(5,6,12,17,18,21)
b=()
c=()
for i in a:
    if i%2==0:
        b=b+(i,)
    else:
        c=c+(i,)
print (a,b,c)