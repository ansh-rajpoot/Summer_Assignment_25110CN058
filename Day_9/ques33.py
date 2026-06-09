#  Write a program to Print reverse star pattern.
# *****
# ****
# ***
# **
# *

n = int(input('Enter the number of rows:- '))
for i in range(0,n):
    for j in range(n-i):
        print('*',end='')
    print()

