# Write a Python program to check whether all dictionaries in a list are empty or not. Sample list : [{},{},{}] Return value : True Sample list : [{1,2},{},{}] Return value : False

dict_list = [{1, 2}, {}, {'apple', 'ball'}]

for items in dict_list:

    if items:

        print("not empty")

    else:

        print("empty")
