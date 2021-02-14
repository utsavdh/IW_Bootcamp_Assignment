# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.
# Sample String  : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12
def uppercase_lowercase_count(string):
    count1 = 0
    count2 = 0
    for char in string:
        if char.isupper():
            count1 = count1 + 1
        elif char.islower():
            count2 = count2 + 1
        else:
            pass
    print(count1, count2)


uppercase_lowercase_count("UtSaV")
