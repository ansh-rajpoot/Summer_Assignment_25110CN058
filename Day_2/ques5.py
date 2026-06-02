# Write a program to Find sum of digits of a number

def sum_digits(n):

    sum=0
    while n>0:
        sum += n%10
        n//=10
    return sum


# Calling the function

n = int(input('Enter the number whose sum of digits you wanna find-'))
sumofdigits = sum_digits(n)
print('sum of digits of the given num is', sumofdigits)