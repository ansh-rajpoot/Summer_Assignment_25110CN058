
# Q27 Write a program to Recursive sum of digits.
def sum(n):
    if  n==0:
        return 0
    return n%10 + sum(n//10)

n= int(input('Enter the num whose sum of digits you wanna find- '))
print('Sum of digits=', sum(n))