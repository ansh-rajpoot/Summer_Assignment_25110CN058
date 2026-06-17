# write a program to intersection of arrays
def intersection_arrays(arr1,arr2):
    arr3=[]
    for element in arr1:
        if element in arr2 and element not in arr3:
            arr3.append(element)
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

print('The intersection of given arrays is', intersection_arrays(arr1,arr2))