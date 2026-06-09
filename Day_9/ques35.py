# Q35 Write a program to Print repeated character
# pattern.
# A
# BB
# CCC
# DDDD
# EEEEE



n = int(input('Enter the number of rows:- '))
for i in range(1,n+1):
    for j in range(i):
        print(chr(64+i),end='')
    print()