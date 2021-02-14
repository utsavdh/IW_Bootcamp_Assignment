string_input = input("Enter any string: ")
final = ""

for i in range(len(string_input)):
    if i % 2 == 0:
        final = final + string_input[i]
print(final)

