#Write a function that converts a binary number to decimal, don’t use ready conversion function.
def coversion():
    binary = input("Enter a binary number: ")
    decimal = 0
    for digit in binary:
        decimal = decimal*2 + int(digit)
    print("The decimal value is:", decimal)
coversion()