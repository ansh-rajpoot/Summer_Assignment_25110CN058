# Q9 Write a program to Check whether a number is prime.

def check_prime(n):
    if n>1:    
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    return False

n= int (input('Enter the number :- '))


if check_prime(n):
    print("Yes, it's a prime number")
else:
    print("No, its not a prime number")