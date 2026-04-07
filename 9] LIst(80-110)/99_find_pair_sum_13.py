#Find the pairs from list whose sum is 13
a=[1,12,1,2,10,3]
for i in range(len(a)):
    if i==len(a)-1:
        break
    else:
        if a[i]+a[i+1]==13:
          print(a[i],a[i+1])
