#Compare two list and display similar numbers from both list L1=[13,12,11] L2=[11,13,14]
L1=[13,12,11]
L2=[11,13,14]
L3=[]
for i in L1:
    if i in L2:
        L3.append(i)
print(L3)