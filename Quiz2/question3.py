'''
Write a function that will print how many times 'hello' is repeated in the string. For example, if s = “hihellohellonohellon”, then the program should print 3. Do not use count.
'''
def count_repeat(s):
    count = 0
    for i in range(len(s)):
        if s[i:i+5] == 'hello':
            count += 1
    print(count)

s="hihellohellonohellon"
count_repeat(s)
