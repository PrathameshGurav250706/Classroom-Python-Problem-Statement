#Display longest word in list using list comprehension


a = ['kolhapur', 'pune', 'mumbai', 'nagpur']
print([word for word in a if len(word) == max([len(word) for word in a]) ])

