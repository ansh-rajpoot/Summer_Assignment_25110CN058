# Q51 Write a program to Find largest and smallest element.
arr=[]
size = int(input("Enter the number of elements you want in the array: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr.append(element)

print("\nThe complete array you entered is:")
print(arr)
if size>0:
    largest=arr[0]
    smallest=arr[0]
    for i in arr:
        if i>largest:
            largest=i
        if i<smallest:
            smallest=i
    print("The largest element is", largest)
    print('The smallest element is', smallest)