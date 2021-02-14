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
