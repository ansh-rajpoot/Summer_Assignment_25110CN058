def selection_sort_descending(arr):
    n = len(arr)
 
    for i in range(n - 1):
        max_index = i
 
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j               
        arr[i], arr[max_index] = arr[max_index], arr[i]
        
    return arr   

arr1 = []
size = int(input("Enter the number of elements you want in the array 1: "))
print(f"Please enter {size} elements:")
for i in range(size):
    element = int(input(f"Element {i+1}: "))
    arr1.append(element)

print("\nThe complete array 1 you entered is:")
print(arr1)
print('the required sorted array is:-', selection_sort_descending(arr1))
