a=5
b=0
try:
    print (a/b)
except ZeroDivisionError:
    print ("mr. egg, don't divide by 0")
finally:
    print ("finish")