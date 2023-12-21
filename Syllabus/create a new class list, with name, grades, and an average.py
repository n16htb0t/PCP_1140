#given class list for a subject: each entry is list of two parts 
# name and last name
# and a list of grades on assignments
# create a new class list, with name, grades, and an average

class_list=[[['John', 'Smith'], [80, 70, 65, 90]], [['Jane', 'Doe'], [100, 85, 90, 95]], [['Michael', 'Green'], [50, 40, 45, 50]]]
def get_stats(class_list):
    new_stats=[]
    for elt in class_list:
        new_stats.append([elt[0], elt[1], avg(elt[1])])
    return new_stats
def avg(grades):
    try:
        return sum(grades)/len(grades)
    except ZeroDivisionError:
        print('no grades data')
        return 0.0
    
print(get_stats(class_list))