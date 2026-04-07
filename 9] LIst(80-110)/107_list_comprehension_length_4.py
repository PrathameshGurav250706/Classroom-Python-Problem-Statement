#Display elements from list having length equal to 4 using list comprehension
a=[1234,456,8685,98475,9087]

print([k for k in a if len(str(k))==4])
