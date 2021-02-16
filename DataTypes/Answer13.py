# 13.Write a Python program that accepts a comma separated sequence of words
#  as input and prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white,red

string_input = input("Enter comma separated word sequence:")
sorted_word_list = sorted(string_input.split(","))
unique_words = set(sorted_word_list)
print(unique_words)
print(",".join(list(unique_words)))