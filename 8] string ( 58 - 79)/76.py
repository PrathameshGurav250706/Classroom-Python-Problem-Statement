#Implement program that accepts a comma-separated sequence of words as input and prints the distinct words in sorted form (alphanumerically). I/P String : red, white, black, red, green, black Expected Result : black, green, red, white, red
a="red, white, black, red, green, black"
a=a.split(',')
word=[]
for i in a:
    if i not in word:
        word.append(i)

word.sort()
print(",".join(word))