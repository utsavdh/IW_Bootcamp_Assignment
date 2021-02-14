# Write a Python program to print the even numbers from a given list.
# Sample List :  [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result  : [2, 4, 6, 8]


def even_no(list1):
    empty_list = []
    for num in list1:
        if num % 2 == 0:
            empty_list.append(num)
        else:
            pass
    return empty_list


print(even_no(range(1, 10)))
