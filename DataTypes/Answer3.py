# 3.  Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

string_input = input("Enter any string: ")

first_character = string_input[0]

string_input = string_input.replace(first_character, '$')
string_input = first_character + string_input[1:]

print(string_input)
