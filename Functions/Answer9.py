# Write a Python function that takes a number as a parameter and check the
# number is prime or not.

def prime_or_not(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")

(prime_or_not(5))