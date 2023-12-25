'''
Write a function that converts a binary number to decimal. If the number is not binary the function should throw an error. Do not use the ready conversion function.
'''
def binary2decimal(n):
    decimal = 0
    i = 0
    while n != 0:
        dec = n % 10
        decimal = decimal + dec * pow(2, i)
        n = n//10
        i += 1
    print(decimal)
n = int(input("Enter a binary number: "))
binary2decimal(n)
