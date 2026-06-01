# Write a program to Print multiplication table of a given number.

n = int(input ("Enter the number whose table you wanna print "))
print('\n The required table of the given number is:- ')

for i in range(1,11):
    print (f"{n}*{i}=", n*i)