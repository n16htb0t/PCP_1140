def fancy_divide(list_of_numbers, index):
    demon= list_of_numbers[index]
    return [simple_divide(item, demon) for item in list_of_numbers]
def simple_divide(item, demon):
    try:
        return item/demon
    except ZeroDivisionError:
        return 0
print(fancy_divide([0,2,4], 0))
print(fancy_divide([0,2,4], 1))