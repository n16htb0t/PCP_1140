a=open("hi.txt","r")
for i in a:
    if i[0]=="h" and "m" in i:
        print (i)
a.close()