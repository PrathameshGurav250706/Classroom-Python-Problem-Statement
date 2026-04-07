#Implement program to remove unwanted characters from a given string.
# I/P String : A%^!B#*CD
#*CD O/P: ABCD

# Example usage of isalnum() method:
# print("Hello123".isalnum())   # True
# print("Hello 123".isalnum())  # False (space present)
# print("Hello@123".isalnum())  # False (special character)
# print("12345".isalnum())      # True
# print("Hello".isalnum())      # True
# print("".isalnum())           # False


a="A%^!B#*CD"
b=""
for i in a:
    if i.isalnum():
        b=b+i   
print(b)    
