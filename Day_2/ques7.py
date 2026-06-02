# Write a program to Find product of digits.
def prod_digits(num):
    prod = 1
    while num>0:
        prod = prod *  (num % 10)
        num //= 10
    return prod

# Calling the function

n = int(input('Enter the num whose product of digits you wanna find'))
product = prod_digits(n)
print('The product of digits of the given num is', product)