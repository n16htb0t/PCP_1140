a=open("hi.txt","r")
lines=0
for i in a:
    lines+=1
print (lines)
a.close()
a=open("hi.txt","r")
b=a.read()
print (len(b))
print (b.count(" ")+lines)
a.close()