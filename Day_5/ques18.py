# Q18 Write a program to Check strong number. 
def check_strong(n):
    sum=0
    temp = n
    while temp>0:
        
        prod=1
        for i in range(1,temp%10+1):
            prod=prod*i
        sum += prod
        temp = temp //10 
    if sum==n:
        return True
    return False

a = int(input('Enter the number:- '))
if check_strong(a):
    print('Yes, its a strong number')
else:
    print('No, its not a strong number')
            
        