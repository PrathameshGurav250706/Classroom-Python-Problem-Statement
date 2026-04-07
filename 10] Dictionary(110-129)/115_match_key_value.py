#WAP to match key values in two dictionaries.
a={1:'abc',2:'def',3:'pqr',4:'xyz'}
b={3:'pqr',4:'xyz'}
for i in a:
    for j in b:
        if i==j and a[i]==b[j]:
            print(f"Found {i} : {a[i]} in both dictionaries")
          

