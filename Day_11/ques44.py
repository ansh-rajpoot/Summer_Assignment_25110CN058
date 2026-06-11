# Write a program Write function to find factorial
def fact(a):
    fac=1
    for i in range(1,a+1):
        fac *=i
    return fac

a= int(input('Enter the num to find the factorial:- '))
print('The factorial of given num is', fact(a))
