# Write a Python script to check whether a given key already exists in a
# dictionary.
dic1 = {1: 10, 2: 20, 'apple': 'iphone'}
dict1_keys = dic1.keys()
# print(key)
key1 = 'ball'
if key1 in dict1_keys:
    print('key exists already')
else:
    print('key does not exists already')
