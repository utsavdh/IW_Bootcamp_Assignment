#  Write a Python script to merge two Python dictionaries.
dict1 = {'a': 100, 'b': 200}
dict2 = {'x': 300, 'y': 200}
dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
