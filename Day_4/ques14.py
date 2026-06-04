# Q.14 Write a program to Find nth Fibonacci term
n = int(input("Enter number of terms: "))
a=0
b=1
for i in range(n):
    if i==(n-1):
        print(a)
    next_term = a+b
    a=b
    b=next_term