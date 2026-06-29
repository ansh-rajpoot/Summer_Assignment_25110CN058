# write  a program to merge two sorted arrays


def merge_sorted_arrays(arr1, arr2):
    n1= len(arr1)
    n2 =len(arr2)
    result = []
    i =0
    j =0
    
    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i+= 1
        else:
            result.append(arr2[j])
            j +=1
            
    while i< n1:
        result.append(arr1[i])
        i += 1
        
    while j< n2:
        result.append(arr2[j])
        j +=1
    return result

size1 = int(input("Enter the number of elements you want in the array 1: "))
arr1 = []
print(f"Please enter {size1} elements:")
for i in range(size1):
    element = int(input(f"Element {i+1}: "))
    arr1.append(element)
arr1.sort()

size2 = int(input("Enter the number of elements you want in the array 2: "))
arr2 = []
print(f"Please enter {size2} elements:")
for i in range(size2):
    element = int(input(f"Element {i+1}: "))
    arr2.append(element)
arr2.sort()

print("\nThe sorted array 1 is:")
print(arr1)
print("The sorted array 2 is:")
print(arr2)
print('\nThe required merged sorted array is:-', merge_sorted_arrays(arr1, arr2))
