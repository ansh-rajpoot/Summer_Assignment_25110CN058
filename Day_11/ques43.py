# Write a program Write function to check prime
def check_prime(n):
    if n <= 1:
        return False
 
    for i in range(2, int(n**(1/2)) + 1):
        if n % i == 0:
            return False   
            
    return True
a= int(input('Enter the num to check for prime:- ')) 
if check_prime(a):
    print("Yes, it's is prime")
else:
    print("No it's not prime")