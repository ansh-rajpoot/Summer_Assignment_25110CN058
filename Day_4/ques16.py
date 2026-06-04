# Q16 Write a program to Print Armstrong numbers in a range.

def is_armstrong(n):
    digits = len(str(n))
    temp = n
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit ** digits

        temp //= 10


    return total == n  

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
print("Armstrong numbers are:")

for i in range(start, end + 1):
    if is_armstrong(i):
        print(i, end=" ")