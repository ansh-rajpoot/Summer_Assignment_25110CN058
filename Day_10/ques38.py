# Q38 Write a program to Print reverse pyramid.
n= int(input('Enter the number of rows:- '))
for i in range(1,n+1):
    for j in range(i-1):
        print(' ',end='')
    for k in range(n+1-i):
        print('*',end='')
    for  l in range(n-i):
        print('*',end='')
    print()