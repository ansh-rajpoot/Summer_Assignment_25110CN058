# Write a program Write function for perfect number
def is_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum += i
    if sum==n:
        return True
    return False

a = int(input('Enter the number:- '))

if a<1:
    print("Please enter the integer greater than 1")
    
else:
    if is_perfect(a):
        print('Yes, its a perfect number')
    else:
        print('No, its not a perfect number')