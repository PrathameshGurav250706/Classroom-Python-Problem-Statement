# Implement program to count Uppercase, Lowercase, special characters and numeric values in a given string.
s = "PrathameshGurav@123"

uppercase_count = 0
lowercase_count = 0
special_count = 0
numeric_count = 0

for i in s:
    if i.isupper():
        uppercase_count += 1
    elif i.islower():
        lowercase_count += 1
    elif i.isdigit():
        numeric_count += 1
    else:
        special_count += 1

print("Uppercase:", uppercase_count)
print("Lowercase:", lowercase_count)
print("Special Characters:", special_count)
print("Numeric Values:", numeric_count)