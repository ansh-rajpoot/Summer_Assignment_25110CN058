# Write a program to Find largest prime factor.
def check_prime(n):
    if n>1:    
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    return False

n = int(input('Enter the number:- '))
largest_prime=0

if n <= 1:
    print("It has no prime factors")

else:
    for i in range(2,n+1):
        if n%i==0 and check_prime(i):
            largest_prime=i
    print('The largest prime factor of given num is ', largest_prime)

        


