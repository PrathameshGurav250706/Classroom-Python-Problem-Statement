#Write a Python program to count the lowercase letters in a given list of words. Sample Data: (["Red", "Green", "Blue", "White"]) count is 13 (["SQL", "C++", "C"]) count is 0
count=0
data=["Red", "Green", "Blue", "White"]
for i in data:
    for j in i:
        if j.islower():
            count+=1

print('lowercase letters count is',count)