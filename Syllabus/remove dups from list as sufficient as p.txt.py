# remove dups from list as sufficient as possible
a=[5,6,7,5,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7]
print(list(dict.fromkeys(a)))


# /// new efficient way

res_list = []
for i in range(len(a)):
    if a[i] not in a[i+1:]:
        res_list.append(a[i])
print(res_list)