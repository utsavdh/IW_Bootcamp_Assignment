given_list = [5, 7, 58, 2, 65, 3, 4, 8, 9]
smallest = given_list[0]
for number in given_list:
    if number < smallest:
        smallest = number
print(smallest)
