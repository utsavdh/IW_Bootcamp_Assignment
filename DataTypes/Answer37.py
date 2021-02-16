# Write a Python program to multiply all the items in a dictionary.

dict1 = {'value1': 5, 'value2': 4, 'value3': 3, 'value4': 2, 'value5': 1, }

mul = 1
for item in dict1:
    mul = mul * dict1[item]
print(mul)
