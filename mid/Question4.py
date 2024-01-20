full = input("Enter your first name and second name:")
names = full.split()
if len(names)==2:
    first, last = names
    format = last.capitalize() + " " + first[0].capitalize() + "."
    print("After Formating",format)
