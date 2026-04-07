#Implement program to count the occurrences of each word in a given sentence.
sentence='one two three one three five'
a=sentence.split()
for i in a:
    print(i,":",a.count(i))