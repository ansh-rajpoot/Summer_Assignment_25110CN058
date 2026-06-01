# Write a program to Count digits in a number.
n = int(input("Enter the num whose digits count you wanna know- "))
digits=0
if n==0:
    digits =1
while (n>0):
    digits+=1
    n//=10
print(f'Number of digits in the given number is - {digits}')
