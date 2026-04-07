#Write a Python program that creates a list of tuples, each containing a product name and its Qty. Use the filter function to extract products with a Qty greater than 12
# print(list(filter(lambda x:True if x[1]>12 else False,[('pen',10),('Notebook',20),('Pencil',30)])))

print(list(filter(lambda x:True if x[1]>12 else False,[('pen',10),('Notebook',20),('Pencil',30)])))