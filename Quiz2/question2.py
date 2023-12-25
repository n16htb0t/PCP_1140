'''
We have the following dictionary {'a': [], 'b': [], 'c': [], 'd': []}, the program must add one random number to a, one random number to b, 4 random numbers to c and 7 random numbers to d, this must be done automatically in one for, write a function that returns: the key , which contains the most elements, and also the product of all the values.
'''
import random
def addingelements(dict):
    for i in dict:
        if i == 'a':
            dict[i].append(random.randint(1, 100))
        elif i == 'b':
            dict[i].append(random.randint(1, 100))
        elif i == 'c':
            for j in range(4):
                dict[i].append(random.randint(1, 100))
        elif i == 'd':
            for j in range(7):
                dict[i].append(random.randint(1, 100))
    print(str(dict)+'\n')

def dict_max(dict):
    max = 0
    for i in dict:
        if len(dict[i]) > max:
            max = len(dict[i])
            key = i
    print("The key with the most elements is: " +'\t'+ key)
    print("The product of all the values is: " +'\t'+ str(max))
       
dict = {'a': [], 'b': [], 'c': [], 'd': []}
addingelements(dict)
dict_max(dict)