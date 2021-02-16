# 11. Write a Python program to count the occurrences of each word in a given
# sentence.
string_input = input("Enter any string: ")
counts = dict()
words = string_input.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)