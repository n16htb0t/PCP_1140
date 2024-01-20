a=open("hi.txt","r")
b=a.read()
print (len(b), b.count("\n"), b.count(" ")+b.count("\n"))
a.close()