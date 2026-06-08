# Q31 Write a program to Print character triangle.
# A
# AB
# ABC
# ABCD
# ABCDE

n= int(input('Enter the number of rows: '))
for i in range(1,n+1):
     
    for j in range(1,i+1):
        print(chr(64+j),end='')
    print()
    