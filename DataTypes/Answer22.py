# Write a  Python program to remove duplicates from a list.

given_list = [1, 2, 5, 8, 1, 12, 5, 2, 8, 49, 62, 30, 1, 2, 5]

new_list = []

for items in given_list:

    if items not in new_list:
        new_list.append(items)

print(new_list)
