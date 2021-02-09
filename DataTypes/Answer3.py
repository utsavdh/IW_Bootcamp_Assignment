string_input = input("Enter any string: ")

first_character = string_input[0]

string_input = string_input.replace(first_character, '$')
string_input = first_character + string_input[1:]

print(string_input)
