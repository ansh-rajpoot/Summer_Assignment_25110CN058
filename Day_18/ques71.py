def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

arr1 = []
size = int(input("Enter the number of elements you want in the array 1: "))
 
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr1.append(element)

arr1.sort()
print("\nThe sorted array 1 used for search is:")
print(arr1)

target_val = int(input("Enter the element you want to search for: "))
result = binary_search(arr1, target_val)

if result != -1:
    print(f"Element found at index:- {result}")
else:
    print("Element not found!")
