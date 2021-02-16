# Write a Python program to create a lambda function that adds 15 to a givennumber passed in as an argument,
# also create a lambda function that multiplicities x with argument y and print the result.

result1 = lambda num1: num1 + 15
result2 = lambda num1, num2: num1*num2

print(result1(15))
print(result2(15,20))
