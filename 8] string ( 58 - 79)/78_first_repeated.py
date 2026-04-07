#Implement program to find the first repeated word in a given string.
# I/P String : ab ca bc ab" O/P : ab
string="ab ca bc ab"
a=string.split()
for i in a:
    if a.count(i)>=2:
        print(i)
        break
