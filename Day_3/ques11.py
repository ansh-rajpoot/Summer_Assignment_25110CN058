# Write a program to Find GCD of two numbers. 

def find_gcd(n,m):
    gcd=1
    if n>m:
    
        for i in range(1,m+1):
            if n%i==0 and m%i==0:
                gcd=i
        return gcd
    else:
        for i in range(1,n+1):
            if n%i==0 and m%i==0:
                gcd=i
        return gcd

a=int(input('Enter 1st number:-'))
b= int(input('Enter 2nd number:-'))
print('The GCD of the given two numbers is', find_gcd(a,b))