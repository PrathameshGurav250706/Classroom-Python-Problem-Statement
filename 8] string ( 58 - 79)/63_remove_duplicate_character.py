# Implement program to remove duplicate characters from a given string
s = "programming"
result = ""

for i in s:
    if i not in result:
        result += i

print(result)


