# 6.​ Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.
# Sample String : 'The lyrics is not that poor!'
# 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
# 'The lyrics is poor!'

str_input=input("Enter any string: ")

str_not = str_input.find('not')
str_poor = str_input.find('poor')

print(str_not)
print(str_poor)

if (str_not < str_poor) and str_not > 0 and str_poor > 0:
    str_input = str_input.replace(str_input[str_not:(str_poor+4)], 'good')
    print(str_input)
else:
    print(str_input)
