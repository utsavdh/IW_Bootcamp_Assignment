string_input1 = input("Enter the first string: ")
string_input2 = input("Enter the second string: ")

swap1 = string_input2[0:2] + string_input1[2:]
swap2 = string_input1[0:2] + string_input2[2:]

print(swap1+' '+swap2)