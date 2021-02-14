# Write a Python function that takes a list and returns a new list with unique
# elements of the first list.
# Sample List :  [1,2,3,3,3,3,4,5]
# Unique List :  [1, 2, 3, 4, 5]

def unique_list(list_item):
    new_list=[]
    for items in list_item:
        if items not in new_list:
            new_list.append(items)
        else:
            pass
    return new_list

unique_list([1,2,2,3,3,3,4,4,4,4])