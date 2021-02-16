# 9.  Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.
string_input = input("Enter any string: ")
first_char=string_input[0]
print(first_char)
last_char=string_input[-1]
print(last_char)

print(last_char+string_input[1:-1]+first_char)
