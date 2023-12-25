# Write a Fibonacci function where we pass the number of months as a parameter and we have to return the number of rabbits. Answers should be recorded to a file.

def Fibonacci():
    file=open("Fibonacci.txt","w")
    months=int(input("Enter the number of months: "))
    file.write("The number of months is: "+str(months)+'\t')
    rabbits=0
    previous=1
    current=1
    for i in range(months):
        rabbits=previous+current
        previous=current
        current=rabbits
        file.write( "Rabbits:" + str(rabbits) +'\n')
    file.close()
    print("The number of rabbits is: ",rabbits)
Fibonacci()
