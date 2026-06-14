# Q52 Write a program to Count even and odd elements.
arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
if size>0:
    odd_elements=0
    even_elements=0
    for i in arr:
        if i %2==0:
            even_elements+=1
        else:
            odd_elements+=1
    print("Numbers of ODD element in the array is", odd_elements)
    print("Numbers of EVEN element in the array is", even_elements)