# The program must generate a random number: 0, 1 or 2. If it generates 0, it must calculate the multiplication of two numbers with for, if it generates 1, it must calculate the factorial of the number while, if it generates 2, it must count the multiplication recursively. In the case of loop don’t use multiplication.

import random
def main():
    number = random.randint(0, 2)
    if number == 0:
        multiply_twono_with_For()
    elif number == 1:
        factorial()
    elif number == 2:
        recursively_multiply()
def multiply_twono_with_For():
    print("The program will multiply two numbers with for loop")
    number1 = int(input("Enter the first number : "))
    number2 = int(input("Enter the second number: "))
    result = 0
    for i in range(number2):
        result += number1
    print("The result is: ", result)
def factorial():
    print("The program will calculate the factorial of the number with while loop")
    number = int(input("Enter the number: "))
    result = 1
    while number > 0:
        result *= number
        number -= 1
    print("The result is: ", result)
def recursively_multiply():
    print("The program will multiply two numbers recursively")
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    def multiply(number1, number2):
        if number2 == 0:
            return 0
        return number1 + multiply(number1, number2 - 1)
    print("The result is: ", multiply(number1, number2))
main()