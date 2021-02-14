def add_string(bracket, word):
    return bracket[:2] + word + bracket[-2:]


print(add_string('{{}}', 'python'))
print(add_string('<<>>', 'python'))
