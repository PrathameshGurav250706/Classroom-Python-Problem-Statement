# Operations on array

import array as s
a=s.array('i',[3,44,2,4,565,4,5,63,48])

# a.append(9)
# a.insert(0,99)        #add element at particular place
# a.extend([10,11,12,13])

# a.remove(13)
# a.pop(3)
# a.pop()      remove last element

# print(a.count(2))
# print(len(a))
# print(a.index(10))

# print(a)

a=s.array('i',sorted(a))
a.reverse()

print(a)