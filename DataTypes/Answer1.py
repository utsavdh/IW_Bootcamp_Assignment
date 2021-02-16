# 1. Write a Python program to count the number of characters (character
# frequency) in a string. Sample String : google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}

string_input = input("Enter any string: ")

frequency_count = {}

for character in string_input:
    if character in frequency_count:
        frequency_count[character] += 1
    else:
        frequency_count[character] =1

print(frequency_count)