# Write a program to Calculate sum of first N natural numbers

def sum_natural(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum



try :
    n= int(input("Enter num till you wanna find the sum "))
    if n < 1:
        print('Please enter number greater than or equal to 1')
    else:
        print(f'the sum of first {n} natural numbers is-', sum_natural(n))
        

except ValueError:
    print("Invalid Input")
