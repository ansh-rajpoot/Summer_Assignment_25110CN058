# Q25 Write a program to Recursive factorial.
def factorial(n):
        if n==0 or n==1:
                return 1
        return n*factorial(n-1)

n = int (input('Enter the num whose factorial you wanna find- '))
print('The factorial of the given number is-', factorial(n))