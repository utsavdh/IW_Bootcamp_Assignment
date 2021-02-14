string_input = input("Enter any string: ")
first_char=string_input[0]
print(first_char)
last_char=string_input[-1]
print(last_char)

print(last_char+string_input[1:-1]+first_char)
