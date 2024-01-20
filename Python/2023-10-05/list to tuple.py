def convert(a):
    b=()
    for i in a:
        b=b+(i,)
    return b
print (convert([5,12,12,17]))