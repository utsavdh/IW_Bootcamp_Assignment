# Sort a list of tuples using Lambda

marks = [('English', 60), ('Maths', 45), ('Nepali', 72)]
print("Original list of tuples", marks)
marks.sort(key = lambda x: x[1])
print("\nSorting the List of Tuples:")
print(marks)
