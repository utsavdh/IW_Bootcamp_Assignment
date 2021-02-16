# 8.  Write a Python program to remove the n​ th​ index character from a nonempty
# string.

string_input = input("Enter any string: ")
nth_index = int(input("Enter the index you want to remove: "))
first_part = string_input[:nth_index]
second_part = string_input[nth_index+1:]
modified_string = first_part+second_part
print(modified_string)
