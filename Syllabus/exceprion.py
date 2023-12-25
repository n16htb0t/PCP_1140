while True:
    try:
        n=int(input("Enter a number: "))
        break
    except ValueError:
        print("Input not an integer; try again")
print("Correct input of an integer!")