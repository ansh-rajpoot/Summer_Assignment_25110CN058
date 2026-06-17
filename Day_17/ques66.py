# Write a program to union of arrays

def union_array(arr1, arr2):
    arr3 = []
 
    combined = arr1 + arr2 
    
    for element in combined:
        if element not in arr3:
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

print('The union of given arrays is', union_array(arr1,arr2))