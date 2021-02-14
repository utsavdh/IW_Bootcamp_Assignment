string_input = input("Enter any string: ")
counts = dict()
words = string_input.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(counts)