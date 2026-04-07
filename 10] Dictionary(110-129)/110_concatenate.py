# 1.WAP to concatenate the two dictionaries to create a new one.
a={1:'abc',2:'def'}
b={3:'pqr',4:'xyz'}
result=a.copy()
result.update(b)
print(result)