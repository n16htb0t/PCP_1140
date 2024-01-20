#1.	You have the following list: [[12,6],[11,5],[3,7],[2,2]].
#The program must calculate the average value of this list. The solution must be as short as possible. The answer must be: 6.
a = [[12, 6], [11, 5], [3, 7], [2, 2]]
sum = 0
for i in a:
    sum += i[1]
average = sum / len(a)
print(average)
