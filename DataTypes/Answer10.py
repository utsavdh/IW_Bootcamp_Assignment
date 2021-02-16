# 10. Write a Python program to remove the characters which have odd index
# values of a given string.
string_input = input("Enter any string: ")
final = ""

for i in range(len(string_input)):
    if i % 2 == 0:
        final = final + string_input[i]
print(final)

