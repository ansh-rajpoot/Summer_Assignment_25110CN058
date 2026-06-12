# Write a program Write function for fibonacci

def get_fibonacci_sequence(n):
    a=0
    b=1
    l=[]
    for i in range(n):
        l.append(a)
        next_term=a+b
        a=b
        b=next_term
    return l






n = int(input("Enter number of terms: "))
print('The required fibonacci sequence :-', get_fibonacci_sequence(n))