# Write a program to Reverse a number.


def reverse_num(num):
    rev = 0
    while num > 0:
         
        rev = rev * 10 + num%10
        num //= 10
    return rev

# Calling the function

n = int ( input('Enter the number whose reverse you wanna find- '))
reverse = reverse_num(n)
print('The reverse of the given num is', reverse)