# 15. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

def add_string(bracket, word):
    return bracket[:2] + word + bracket[-2:]


print(add_string('{{}}', 'python'))
print(add_string('<<>>', 'python'))
