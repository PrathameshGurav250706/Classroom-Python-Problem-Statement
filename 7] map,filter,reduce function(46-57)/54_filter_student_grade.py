#Write a Python program that creates a list of dictionaries containing student information (name, age, grade) and uses the filter function to extract students with a grade greater than or equal to 95. 
# Use following list 
students = [ {"name": "ABC", "age": 18, "grade": 97}, {"name": "PQR", "age": 16, "grade": 92}, {"name": "XYZ", "age": 17, "grade": 90}, {"name": "TEST", "age": 16, "grade": 94}]

print(list(filter(lambda x:True if x['grade']>=95 else False,students)))

