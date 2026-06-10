# Q40 Write a program to Print character pyramid.

n= int(input('Enter the number of rows:- '))
for i in range(1,n+1):
    for j in range(n-i):
        print(' ',end='')
    for k in range(1,i+1):
        print(chr(64+k),end='')
    for  l in range(i-1,0,-1):
        print(chr(64+l),end='')
    print()