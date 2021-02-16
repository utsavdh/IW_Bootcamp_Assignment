# Write a Python program to sort a list of dictionaries using Lambda.

list1 = [{"name": "Nil", "age": 21},
         {"name": "Nitin", "age": 19},
         {"name": "Mukesh", "age": 22}]
sort = sorted(list1, key=lambda i: i['age'])
print("The list printed sorting by age: ")
print(sort)
