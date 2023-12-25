def isPal(x):
    assert type(x) == list
    
    temp = ''.join(x)  
    print(temp)
    temp_reverse = temp[::-1]  
    print(temp_reverse)
    if temp == temp_reverse:
        return True
    else:
        return False
            
def silly(n):
    for i in range(n):
        result=[]
        elem=input("Enter an element")
        result.append(elem)
    if isPal(result):
        print('Yes')
    else:
        print('No')

print(isPal(["a","b","c","b","c"]))
