#WAP to filter a dictionary based on values
a={1:'abc',2:'def',3:'abbsc',4:"jfjf",5:'fjj'}
empty={}
for i,j in a.items():
    if i>2:
        empty[i]=j
print(empty)
    