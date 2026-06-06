# Write a program to Convert binary to decimal.
def binary_decimal(n):
    decimal =0
    i = 0

    while n >0:


        rem = n%10   
        x = rem*(2**i)
        decimal = decimal + x
        n=n // 10
        i+=1
    return decimal



a =int(input("enter binary : "))

ans =binary_decimal(a)
print("binary :",a)

print("decimal :",ans)