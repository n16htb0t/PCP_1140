#We have an empty tuple that the program has to fill with 50 random elements, then the program has to move the even elements in one tuple, the odd elements in the second tuple, and the elements in the third tuple that are divisible by 3. Save the received tuples to a file, every tuple on a separate line. The program must be done using the function.

import random

def is_even(x):
    return x % 2 == 0

def is_odd(x):
    return x % 2 != 0

def is_multiple_of_three(x):
    return x % 3 == 0

def random1():
    tuple1 = random.sample(range(1, 100), 50)
    tuple2 = tuple(filter(is_even, tuple1))
    tuple3 = tuple(filter(is_odd, tuple1))
    tuple4 = tuple(filter(is_multiple_of_three, tuple1))

    with open("tuple.txt", "w") as file:
        file.write("tuple1" + ':'+ '\t'+   str(tuple1) +  "\n")
        file.write("tuple2" + ':'+ '\t'+   str(tuple2) +  "\n")
        file.write("tuple3" + ':'+ '\t'+   str(tuple3) + "\n")
        file.write("tuple4" + ':'+ '\t'+  str(tuple4) +   "\n")

random1()
