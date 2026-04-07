#Perform all the methods set.
a={1,2,3,4,5}
b={5,6,7,8,9,10}

print("Union of a and b :",a.union(b))

a.pop()
print("After pop operation",a)

a.add(11)       #in set instead of append we use add method to add the element.
print("after adding new element :",a)

a.remove(2)
print("After removing value 2 :",a)

print("Intersection between a & b :",a.intersection(b))

print("No Common elemnt :",a.isdisjoint(b))

print("is a subset of b :",a.issubset(b))

c=a.copy()
print("Copy of a :",c)