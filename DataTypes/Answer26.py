# Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4],
# string : emp Expected
# output : ['emp1', 'emp2', 'emp3', 'emp4']

given_string= input("enter the string:")

sample_list= [1,2,3,4]

empty_list=[]

for items in sample_list:

    sample_list=given_string+ str(items)

    empty_list.append(sample_list)

print(empty_list)