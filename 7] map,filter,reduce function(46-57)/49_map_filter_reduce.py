# we cannot use list for reducen function to convert in string and use import functools


# input 10 no.s, calculate square of each number, find out only odd square and find out the sum of all odd square
import functools
print(functools.reduce(lambda a,b:a+b,list(filter(lambda y:True if y%2!=0 else False,list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9,10]))))))

# list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9,10]))

# list(filter(lambda y:True if y%2!=0 else False,list(map(lambda x:x*x,[1,2,3,4,5,6,7,8,9,10]))))

# import functools
# print(list(map(lambda x: x**2,[1,2,3,4,5,6,7,8,9,10])))
# print(list(filter(lambda y:True if y%2!=0 else False,list(map(lambda x: x**2,[1,2,3,4,5,6,7,8,9,10])))))
# print(functools.reduce(lambda p1,p2: p1+p2,list(filter(lambda y:True if y%2!=0 else False,list(map(lambda x: x**2,[1,2,3,4,5,6,7,8,9,10]))))))

