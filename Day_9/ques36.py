# Q36 Write a program to Print hollow square
# pattern.
#  *****
#  *   *
#  *   *
#  *   *
#  *****

n = int(input('Enter the number of sides of a square:- '))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n:
            print('*',end='')
        else:
            if j==1 or j==n:
                print('*',end='')
            else:
                print(' ',end='')
    print()