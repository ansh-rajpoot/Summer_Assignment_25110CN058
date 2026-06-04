# Q15 Write a program to Check Armstrong number.


def is_armstrong(n):
    digits = len(str(n))
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits

        temp //= 10


    return total == n 

n = int(input("Enter a number: "))
if is_armstrong(n):
    print("Yes, Armstrong Number")
else:
    print("No, Not an Armstrong Number")