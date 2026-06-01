# Write a program to Find factorial of a number.
n = input("Enter num whose factorial you wanna find ")
fact = 1
for i in range(int(n),0,-1):
    fact *=i
print(f'\n The factorial of {n} is - {fact} \n')