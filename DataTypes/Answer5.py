# 5.Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc'
# Expected Result : 'abcing'
# Sample String : 'string'
# Expected Result : 'stringly'

string_input = input("Enter any string: ")

length=len(string_input)

if length>3:
    if string_input[-3:]=='ing':
        string_input=string_input+'ly'
    else:
        string_input=string_input+'ing'

print(string_input)