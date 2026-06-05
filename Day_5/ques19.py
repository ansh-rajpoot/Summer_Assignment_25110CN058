# Q19 Write a program to Print factors of a number. 
n = int(input('Enter the number:- '))
print('The factors of given numbers are-', end =' ')
if n<1:
    print("Please enter number greater than or equal to 1")
else:
    for i in range(1,n+1):
        if n %i==0:
            print(i, end=', ')
