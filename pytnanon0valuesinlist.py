#[5,6,7,2]
#[5,6,8,0,2]
#put nan in place of 0

# data=[5,6,7,0,3]
# for i in range(len(data)):
#     if data[i]==0:
#         data[i]=float('nan')
# print(data)


def get_ratios(L1,L2):
    ratios=[]
    for index in range(len(L1)):
        try:
            ratios.append(L1[index]/L2[index])
        except ZeroDivisionError:
            ratios.append(float('nan'))
        except:
            raise ValueError('get_ratios called with bad arg')
    return ratios
L1=[5,6,7,0,3]
L2 = [5,6,8,0,2]
print(get_ratios(L1,L2))