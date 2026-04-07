# w.a.p to find the entered characher is a consonants and vowels
vowels='aeiouAEIOU'
s=input("Enter a character : ")
for i in vowels:
    if i==s:
        print('Vowel')
        break
else:
    print('consonants')
