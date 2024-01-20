a=[5,6,7,8]
try:
    print (a[5])
except IndexError as e:
    print ("count the elements",e)
finally:
    print ("finish")
