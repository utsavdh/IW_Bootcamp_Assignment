string_input = input("Enter any string: ")

frequency_count = {}

for character in string_input:
    if character in frequency_count:
        frequency_count[character] += 1
    else:
        frequency_count[character] =1

print(frequency_count)