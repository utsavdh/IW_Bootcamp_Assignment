# Write a Python function to multiply all the numbers in a list.
# Sample List :  (8, 2, 3, -1, 7)
# Expected Output  : -336
def product_list(list_items):
    mul = 1
    for numbers in list_items:
        mul = mul * numbers
    print(mul)


product_list([2, 5, 6, 7, -1])