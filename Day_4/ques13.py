# Q13 Write a program to Generate Fibonacci series.
n = int(input("Enter number of terms: "))
a=0
b=1
for i in range(n):
    print(a,end=' ')
    next_term=a+b
    a=b
    b= next_term
