# Write a Python program to reverse a string.
# Sample String  : "1234abcd"
# Expected Output  : "dcba4321"

def reverse_string(string_input):
    string = string_input[::-1]
    return string


print(reverse_string("Hello world!"))
