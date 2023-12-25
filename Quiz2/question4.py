'''
Write a function that takes a number as a parameter and converts that number to binary, do not use bin function.
'''
def decimal2binary(n):
    if n > 1:
        decimal2binary(n//2)
    print(n % 2,end = '')
n = int(input("Enter a decimal number: "))
decimal2binary(n)
print()
