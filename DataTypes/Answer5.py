string_input = input("Enter any string: ")

length=len(string_input)

if length>3:
    if string_input[-3:]=='ing':
        string_input=string_input+'ly'
    else:
        string_input=string_input+'ing'

print(string_input)