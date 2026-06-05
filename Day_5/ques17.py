# Q17 Write a program to Check perfect number.
def check_perfect(n):
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
    if check_perfect(a):
        print('Yes, its a perfect number')
    else:
        print('No, its not a perfect number')