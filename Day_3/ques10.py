# Write a program to Print prime numbers in a range.

def check_prime(n):
    if n>1:    
        for i in range(2,n):
            if n%i==0:
                return False
        return True
    return False

start =int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Prime numbers in the given range are:- ")
for i in range(start,end+1):
    if check_prime(i):
        print(i, end=(', '))
