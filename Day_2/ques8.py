# Write a program to Check whether a number is palindrome.


def reverse_num(num):
    rev = 0
    while num > 0:
         
        rev = rev * 10 + num%10
        num //= 10
    return rev


num = int(input('Enter the number for which you wanna check if it is Palindrome or not- '))
if num == reverse_num(num):
    print('Yes, its a Palindrome')
else:
    print('No, its not a Palindrome')