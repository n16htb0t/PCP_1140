#2.	You have the following list: [[“hi”,6],[“hi”,5],[“yes”,7],[“no”,2]]. The program must print two lists: [6,5,7,2] –only the numbers and [“hi”,”yes”,”no”] – the unique words. The solution must be as short as possible.
a= [["hi", 6], ["hi", 5], ["yes", 7], ["no", 2]]
num=[]
words=[]
for i in a:
    num.append(i[1])
    words.append(i[0])
print(words)
print(num)