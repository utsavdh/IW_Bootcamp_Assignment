string_input = input("Enter any string: ")

string = ""

if len(string_input)<=2:
    print(string)

else:
    print(string_input[0:2]+string_input[-2:])