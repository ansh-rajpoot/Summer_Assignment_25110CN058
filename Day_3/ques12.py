# Write a program to Find LCM of two numbers.
def find_lcm(a,b):
    if a>b:
        lcm=a
        step=a
    else:
        lcm=b
        step=b
    while True:
        if lcm%a==0 and lcm%b==0:
            return lcm
        lcm += step


n=int(input('Enter 1st number:-'))
m= int(input('Enter 2nd number:-'))
print('The lcm of the given num is ', find_lcm(n,m))