# Write a program to Convert decimal to binary
def decimal_binary(n):
    if n == 0:
        return ""
    
    if n>0:
        c = n%2
        d = n //2
        return decimal_binary(d) +str(c)
    
    
a =int(input("enter the number which you want to convert in binary : "))
if a==0:
    print("binary : 0")
else:
    result = decimal_binary(a)
    print("decimal :", a)
    print("binary :", result)