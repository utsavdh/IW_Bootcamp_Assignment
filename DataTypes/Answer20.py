str_list = ['abc', 'xyz', 'aba', '1221']
count = 0
for item in str_list:
    if len(item) >= 2 and item[0] == item[-1]:
        count += 1

print("The no. of strings where string length is 2 or more and the first and last character are same is:", count)
