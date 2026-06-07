# Q28 Write a program to Recursive reverse number.
 

def reverse(n, m):
    if n ==0:
        return m
    return reverse(n //10, m * 10 + n % 10)

n = int(input("Enter the number: "))
print("Reversed of given number =", reverse(n, 0))