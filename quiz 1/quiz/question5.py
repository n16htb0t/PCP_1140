#5.	The program must input a string and count the number of characters “b” in this string. If the received number is more than five, it should be written to us - "many". If it is less than five, the program continues reading, until the number of b - characters in the string we entered is greater than or equal to 5. If the received number is equal to five, the program must count the sum of all numbers from 1 to 20.

while True:
    i=input("Enter a string")
    count=i.count("b")
    if count >5:
        print("many")
        break
    elif count <5:
        print("Not enough")
    else:
        sum=0
        for i in range(1,21):
            sum+=i
        print(sum)
        break