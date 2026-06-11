# Write a program Write function to find to maximum.
def find_max(a,b):
    if a>b:
        return a
    return b

a=int(input('Enter first number:- '))
b= int(input('Enter second number:- '))
print('The maximum number is', find_max(a,b))