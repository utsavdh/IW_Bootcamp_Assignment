
# Write a Python function to find the Max of three numbers.
def max_of_two(num1, num2):
    if num1 > num2:
        return num1
    return num2


def max_of_three(num1, num2, num3):
    print( "the maximum no is:", max_of_two(max_of_two(num1, num2), num3))



max_of_three(7,2,3)