# Implement program to count and display vowels in text.
a='prathamesh'
vowel='aeiouAEIOU'
count=0
for i in a:
    if i in vowel:
        count+=1
print('Numbers of vowel present in text is',count)
