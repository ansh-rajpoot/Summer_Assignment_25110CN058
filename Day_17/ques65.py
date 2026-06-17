# write a program to merge arrays
def merge_array(arr1, arr2):
    arr3=[]
    for i in arr1:
        arr3.append(i)
    for j in arr2:
        arr3.append(j)
    return arr3

arr1 = []
size = int(input("Enter the number of elements you want in the array 1: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr1.append(element)

print("\nThe complete array 1 you entered is:")
print(arr1)

arr2 = []
size = int(input("Enter the number of elements you want in the array 2 : "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr2.append(element)

print("\nThe complete array 2 you entered is:")
print(arr2)

print('The merged array is', merge_array(arr1,arr2))