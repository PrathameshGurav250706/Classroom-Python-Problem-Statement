#WAP to find the two numbers whose product is maximum among all the pairs in a given set of numbers?
a={1,2,10,4,5}
b=list(sorted(a))
length=len(b)
print(f"{b[length-1] } and { b[length-2] } have the maximum product")
