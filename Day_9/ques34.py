# Q34 Write a program to Print reverse number
# triangle.
# 12345
# 1234
# 123
# 12
# 1
n = int(input('Enter the number of rows:- '))
for i in range(0,n):
    for j in range(1,n-i+1):
        print(j,end='')
    print()