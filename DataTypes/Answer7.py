# 7.Write a Python function that takes a list of words and returns the length of the
# longest one.

string_input=input("Enter any string")
list=string_input.split()
length_list=[]
for words in list:
    length=len(words)
    length_list.append((length,words))

length_list.sort()
print("The longest string is: ",length_list[-1][1] + " and its length is: ",length_list[-1][0])