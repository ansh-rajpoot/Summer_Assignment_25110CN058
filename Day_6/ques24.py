# Q24 Write a program to Find x^n without pow().

x = int(input("Enter the number (x): "))
n = int(input("Enter the power (n): "))

result = 1

for i in range(n):
    result *= x

print(f"{x}^{n} =", result)