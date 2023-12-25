data =[]
filename = "list.txt"
try:
    fh = open(filename, 'r')
except IOError: 
    print('cannot open', filename)
else:
    for new in fh:
        if new != '\n':
            addIt = new[:-1].split(',') 
            data.append(addIt) 




finally:
    fh.close()

gardesData = []
if data:
    for student in data:
        try:
            gardesData.append([student[0:2], [student[2]]])
        except IndexError:
            gardesData.append([student[0:2], []])
print (gardesData)

print('-------------------')

gardesData=[]
for student in data:
    try:
        name = student[0:-1]
        grades = int(student[-1])
        gardesData.append([name, [grades]])
    except ValueError:
        gardesData.append([student[:], []])

print(data)
print('-------------------')
print(gardesData)